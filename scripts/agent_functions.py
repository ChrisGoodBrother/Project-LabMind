from autogen import ConversableAgent

def saveCodeToFile(logger, final_output):
    # --- Save code to a file ---
    import re

    code_blocks = re.findall(r"```(?:python)?\n([\s\S]*?)```", final_output)

    if code_blocks:
        code_to_save = "\n\n".join(code_blocks)
        save_path = os.path.join(os.getcwd(), "generated_code.py")
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(code_to_save)
        logger.info("✅ Code saved to %s", save_path)
    else:
        logger.warning("⚠️ No code block found in the final output.")

def createAgent(name, message, description, llm_config, terminationMessage=None):
    agent = ConversableAgent(
        name=name,
        system_message=message,
        description=description,
        is_termination_msg=terminationMessage,
        llm_config=llm_config,
    )

    return agent
