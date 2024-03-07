import { invokeChain, ChatResponse, ChatHistory } from "./client.js";

const history: ChatHistory[] = [
    {
      role: 'human',
      content: 'What are the different volunteering events at CAPT?'
    },
    {
      role: 'ai',
      content: 'At CAPT, there are various volunteering events and projects organized by the ACE (Arts, Culture, and Environment) committee. Some of the projects include event photography and facilitating academic events like CAPTISS 2021, as well as other community engagement and active citizenship initiatives. These projects provide opportunities for CAPTains to learn, share, and empower themselves while serving the community. You can find more information and sign-up forms for all projects by clicking on the provided links in the announcements.'
    }
  ]
const response: ChatResponse = await invokeChain(history, "What are the different volunteering events at CAPT?")
console.log(response)