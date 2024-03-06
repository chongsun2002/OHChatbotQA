import { invokeChain, ChatResponse } from "./client.js";

const response: ChatResponse = await invokeChain([], "What are the different volunteering events at CAPT?")
console.log(response)