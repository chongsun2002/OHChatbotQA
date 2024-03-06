from chatbot import retrieval_chain
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(
    title="Chatbot Server",
    version="1.0",
    description="Open House Chatbot Server"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

add_routes(
    app,
    retrieval_chain,
    path="/ask",
)

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="localhost", port=8000)uvicorn main:app --port 5000