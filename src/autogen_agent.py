from autogen_agentchat.messages import TextMessage
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient


class MyAssistant(RoutedAgent):
    """
    ...
    """

    def __init__(self, name: str) -> None:
        """
        ...
        """
    
        super().__init__(name)
    
        model_client = OpenAIChatCompletionClient(model="gpt-4o")
        self._delegate = AssistantAgent(name, model_client=model_client)

    @message_handler
    async def handle_my_message_type(
        self,
        message: MyMessageType,
        ctx: MessageContext
    ) -> None:
        """
        ...
        """

        print(f"{self.id.type} received message: {message.content}")

        response = await self._delegate.on_messages(
            [TextMessage(content=message.content, source="user")], ctx.cancellation_token
        )

        print(f"{self.id.type} responded: {response.chat_message.content}")



# main.py
runtime = SingleThreadedAgentRuntime()
await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

runtime.start()  # Start processing messages in the background.
await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))

