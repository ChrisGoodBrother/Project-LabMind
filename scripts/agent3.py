import agent_functions

def get_agent(llm_config):
    trip_decider_name = "trip_decider"
    trip_decider_message = "You are a trip plan decider. Decide on a final trip plan by collaborating with the trip planner and reviewer"
    trip_decider_desc = "Decides on a final traveling plan"
    trip_decider_termination_message = lambda x: "DONE!" in (x.get("content", "") or "").upper()
    return agent_functions.createAgent(trip_decider_name, trip_decider_message, trip_decider_desc, llm_config, trip_decider_termination_message)
