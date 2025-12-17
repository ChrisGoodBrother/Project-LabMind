import logging
from autogen import LLMConfig
from autogen.agentchat import run_group_chat
import os
from autogen.agentchat.group.patterns import AutoPattern
import json
import agent_functions
import sys
import importlib.util

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    script_dir = os.path.dirname(__file__)
    # Go one directory up
    parent_dir = os.path.abspath(os.path.join(script_dir, ".."))
    # Build full path to the config file
    config_path = os.path.join(parent_dir, "OAI_CONFIG_LIST.json")

    # Load LLM config
    llm_config = LLMConfig.from_json(path=config_path)

    payload = json.loads(sys.stdin.readline())

    agentModels = payload["agents"]
    first_message = payload["firstMessage"]

    agents = agent_functions.build_agents(agentModels, llm_config)

    auto_selection = AutoPattern(
        agents= agents,
        initial_agent=agents[0],
        group_manager_args={"name": "group_manager", "llm_config": llm_config},
    )
    logger.info(f"Starting Conversation")

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
    main()