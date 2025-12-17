import logging
from autogen import LLMConfig
from autogen.agentchat import run_group_chat
import os
from autogen.agentchat.group.patterns import AutoPattern
import agent_functions
import sys
import importlib.util

def import_agent_from_script(script_path, llm_config):
    spec = importlib.util.spec_from_file_location("agent_module", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.get_agent(llm_config)

def main(agent1_script_path, agent2_script_path, agent3_script_path, first_message="Let's plan a traveling trip from athens to japan"):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    script_dir = os.path.dirname(__file__)
    # Go one directory up
    parent_dir = os.path.abspath(os.path.join(script_dir, ".."))
    # Build full path to the config file
    config_path = os.path.join(parent_dir, "OAI_CONFIG_LIST.json")

    # Load LLM config
    llm_config = LLMConfig.from_json(path=config_path)

    agent1 = import_agent_from_script(agent1_script_path, llm_config)
    agent2 = import_agent_from_script(agent2_script_path, llm_config)
    agent3 = import_agent_from_script(agent3_script_path, llm_config)

    auto_selection = AutoPattern(
        agents=[agent1, agent2, agent3],
        initial_agent=agent1,
        group_manager_args={"name": "group_manager", "llm_config": llm_config},
    )
    logger.info(f"Starting conversation between ${agent1}, ${agent2} and ${agent3}")

    response = run_group_chat(
        pattern=auto_selection,
        messages=first_message,
        max_rounds=10,
    )

    logger.info("Conversation completed. Processing results...")

    response.process()
    final_output = response.summary

    logger.info("Final output:\n%s", final_output)

    agent_functions.saveCodeToFile(logger, final_output)

if __name__ == "__main__":
    main(*sys.argv[1:4])