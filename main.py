import os
from dotenv import load_dotenv
from llama_agents import (
    AgentService,
    AgentOrchestrator,
    ControlPlaneServer,
    SimpleMessageQueue,
)
from llama_index.core.tools.function_tool import FunctionTool
from llama_index.core.agent import ReActAgent
from custom_openai_llm import CustomOpenAILLM  # Import the custom LLM implementation

# Load environment variables from .env file
load_dotenv()

# Ensure OpenAI key is set
openai_key = os.getenv("OPENAI_API_KEY")
if not openai_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# Create an agent
def get_the_secret_fact() -> str:
    """Returns the secret fact."""
    return "The secret fact is: A baby llama is called a 'Cria'."

tool = FunctionTool.from_defaults(fn=get_the_secret_fact)

agent1 = ReActAgent.from_tools([tool], llm=CustomOpenAILLM(model="gpt-4", api_key=openai_key))
agent2 = ReActAgent.from_tools([], llm=CustomOpenAILLM(model="gpt-4", api_key=openai_key))

# Create our multi-agent framework components
message_queue = SimpleMessageQueue(port=8000)
control_plane = ControlPlaneServer(
    message_queue=message_queue,
    orchestrator=AgentOrchestrator(llm=CustomOpenAILLM(model="gpt-4", api_key=openai_key)),
    port=8001,
)
agent_server_1 = AgentService(
    agent=agent1,
    message_queue=message_queue,
    description="Useful for getting the secret fact.",
    service_name="secret_fact_agent",
    port=8002,
)
agent_server_2 = AgentService(
    agent=agent2,
    message_queue=message_queue,
    description="Useful for getting random dumb facts.",
    service_name="dumb_fact_agent",
    port=8003,
)

# Start the servers
if __name__ == "__main__":
    import threading

    def start_service(service):
        service.run()

    threading.Thread(target=start_service, args=(message_queue,)).start()
    threading.Thread(target=start_service, args=(control_plane,)).start()
    threading.Thread.target(start_service, args=(agent_server_1,)).start()
    threading.Thread.target(start_service, args=(agent_server_2,)).start()

    print("All services are running.")
