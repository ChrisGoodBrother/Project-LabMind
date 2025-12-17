import agent_functions

def get_agent(llm_config):
    trip_reviewer_name = "trip_reviewer"
    trip_reviewer_message = "You are a trip plan reviewer. Compare plans given to you and provide 3 best options"
    trip_reviewer_desc = "Compares plans and provides the 3 best traveling plan options"
    return agent_functions.createAgent(trip_reviewer_name, trip_reviewer_message, trip_reviewer_desc, llm_config)
