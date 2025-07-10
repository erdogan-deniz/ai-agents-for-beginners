# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)
agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)
# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")
user_proxy = UserProxyAgent(
    "user_proxy",
    input_func=input
)
team = RoundRobinGroupChat(
    [agent_retrieve, agent_analyze, user_proxy],
    termination_condition=termination,
)
stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
