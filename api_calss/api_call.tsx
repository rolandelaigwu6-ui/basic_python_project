import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const MODEL = process.env.GEMINI_MODEL ?? "gemini-3.8-flash";

const response = await client.models.generateContent({
  model: MODEL,
  contents: "What is a neural network in one sentence?",
});

console.log(response.text);
