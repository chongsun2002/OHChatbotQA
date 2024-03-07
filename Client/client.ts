// import { RemoteRunnable } from "@langchain/core/runnables/remote";
// import { HumanMessage, AIMessage, BaseMessage } from "@langchain/core/messages";
// import { RunnableConfig } from "@langchain/core/dist/runnables/config.js";
import axios from "axios";

export type ChatHistory = {
    role: string
    content: string
}

export type ChatResponse = {
    answer: string
    chat_history: ChatHistory[]
};

// const remoteChain: RemoteRunnable<any, any, RunnableConfig> = new RemoteRunnable({
//     url: "http://127.0.0.1:5000/",//"https://ohchatbot-production.up.railway.app/ask/",
// });

export async function invokeChain(chatHistory: ChatHistory[], question: string): Promise<ChatResponse> {
    // const result = await remoteChain.invoke({
    //     input: question,
    //     chat_history: chatHistory,
    // });
    try {
        const result = await axios.post('http://127.0.0.1:5000/invoke', {
            input: question,
            chat_history: chatHistory
        })
        const chatResponse: ChatResponse = result.data
        return chatResponse;
    } catch (error) {
        console.error(error)
        //console.error("Server error, unable to get answer from chatbot invokation");
        const chatResponse: ChatResponse = {answer: "Unable to generate response, try again later",
                                            chat_history: chatHistory};
        return chatResponse;
    }
}