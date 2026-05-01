import uuid
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser 


from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

prompt=ChatPromptTemplate.from_messages([
    ("system","You are a helpfull assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human","{input}")
])

llm= ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=GOOGLE_API_KEY)
chain= prompt | llm | StrOutputParser()
store={}

def get_session_history(session_id:str):
    if session_id not in store:
        store[session_id]= InMemoryChatMessageHistory()
    return store[session_id]


chat_with_history= RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)



