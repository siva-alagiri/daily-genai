from langchain_core.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

llm = init_chat_model(
    "gemini-2.5-flash-lite",
    model_provider="google_vertexai",
    temperature=0.2,
)

response = llm.invoke(
    [HumanMessage(content="Hello from Vertex AI")]
)

print(response.content)
