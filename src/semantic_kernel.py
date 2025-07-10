# Semantic Kernel Python
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.kernel import Kernel

kernel = Kernel()
kernel.add_service(
  AzureChatCompletion(
      deployment_name="your-deployment-name",
      api_key="your-api-key",
      endpoint="your-endpoint",
  )
)

from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion


async def main():
    from semantic_kernel.functions import KernelFunctionFromPrompt
    from semantic_kernel.kernel import Kernel

    kernel = Kernel()
    kernel.add_service(AzureChatCompletion())

    user_input = input("User Input:> ")

    kernel_function = KernelFunctionFromPrompt(
        function_name="SummarizeText",
        prompt="""
        Summarize the provided unstructured text in a sentence that is easy to understand.
        Text to summarize: {{$user_input}}
        """,
    )

    response = await kernel_function.invoke(kernel=kernel, user_input=user_input)
    print(f"Model Response: {response}")

    """
    Sample Console Output:

    User Input:> I like dogs
    Model Response: The text expresses a preference for dogs.
    """


if __name__ == "__main__":
  import asyncio
  asyncio.run(main())
