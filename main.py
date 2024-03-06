from chatbot import retrieval_chain

from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(
    title="Chatbot Server",
    version="1.0",
    description="Open House Chatbot Server"
)

add_routes(
    app,
    retrieval_chain,
    path="/ask",
)

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="localhost", port=8000)uvicorn main:app --port 5000