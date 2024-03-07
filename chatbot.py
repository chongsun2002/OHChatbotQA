import os

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from langchain_core.prompts import ChatPromptTemplate

from langchain_community.vectorstores import FAISS

from langchain.chains.combine_documents import create_stuff_documents_chain

from langchain.chains import create_history_aware_retriever
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import MessagesPlaceholder

from openai import RateLimitError

from langchain_core.messages import AIMessage, HumanMessage

OPENAI_KEY = os.environ.get("OPENAI_KEY")
embeddings= OpenAIEmbeddings(openai_api_key=OPENAI_KEY)
vector = FAISS.load_local('OHChatbotFAISSOpenAI', embeddings)
retriever = vector.as_retriever()
llm = ChatOpenAI(openai_api_key=OPENAI_KEY)

prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
])

retriever_chain = create_history_aware_retriever(llm, retriever, prompt)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer the user's questions based on the below context:\n\n{context}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
])
document_chain = create_stuff_documents_chain(llm, prompt)

retrieval_chain = create_retrieval_chain(retriever_chain, document_chain)

def ask_question(question, chat_history):
    processed_history = []
    for message in chat_history:
        if message["role"] == "human":
            processed_history.append(HumanMessage(content=message["content"]))
        if message["role"] == "ai":
            processed_history.append(AIMessage(content=message["content"]))
    result = retrieval_chain.invoke({
        "input": question,
        "chat_history": processed_history
    })
    answer = result['answer']
    chat_history.append({
        "role": "human",
        "content": question
    })
    chat_history.append({
        "role": "ai",
        "content": answer
    })
    return {
        "answer": answer,
        "chat_history": chat_history
    }

# print(askQuestion("What types of rooms are available at CAPT?", []))