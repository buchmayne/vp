import os
from dotenv import load_dotenv
import openai
from langchain.llms import OpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)

messages = [
    SystemMessage(content=""),
    HumanMessage(content="")
]

response = chat(messages)

print(response.content)
