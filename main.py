from chatbot import retrieval_chain
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, Response
from langserve import add_routes
from langserve import APIHandler
import json
from chatbot import ask_question

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

# api_handler = APIHandler(retrieval_chain, path="/")

@app.post("/invoke", include_in_schema=False)
async def invoke(request: Request) -> Response:
    s = await request.json()
    answer = ask_question(s['input'], s['chat_history'])
    return answer

# add_routes(
#     app,
#     retrieval_chain, 
#     path='/ask'
# )

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="localhost", port=8000)uvicorn main:app --port 5000