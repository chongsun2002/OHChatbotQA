import { RemoteRunnable } from "@langchain/core/runnables/remote";
import { HumanMessage, AIMessage, BaseMessage } from "@langchain/core/messages";
import { RunnableConfig } from "@langchain/core/dist/runnables/config.js";

export type ChatResponse = {
    response: string
    chatHistory: BaseMessage[]
};

const remoteChain: RemoteRunnable<any, any, RunnableConfig> = new RemoteRunnable({
    url: "https://ohchatbot-production.up.railway.app/ask/",
});

export async function invokeChain(chatHistory: BaseMessage[], question: string): Promise<ChatResponse> {
    const result = await remoteChain.invoke({
        "input": question,
        "chat_history": chatHistory
    });
    try {
        const answer = result.answer;
        chatHistory.push(new HumanMessage(question));
        chatHistory.push(new AIMessage(answer));
        const chatResponse: ChatResponse = {"response": answer, "chatHistory": chatHistory};
        return chatResponse;
    } catch (error) {
        console.error("Server error, unable to get answer from chatbot invokation");
        const chatResponse: ChatResponse = {"response": "Unable to generate response, try again later",
                                            chatHistory: chatHistory};
        return chatResponse;
    }
}