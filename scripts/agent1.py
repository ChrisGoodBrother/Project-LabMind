import agent_functions

def get_agent(llm_config):
    trip_planner_name = "trip_planner"
    trip_planner_message = "You are a trip planner. Give 5 cheap traveling destinations by airplane from athens to japan. Include travel costs and destinations"
    trip_planner_desc = "Gives 5 cheap traveling destinations by airplane"
    return agent_functions.createAgent(trip_planner_name, trip_planner_message, trip_planner_desc, llm_config)
