import OpenAI from "https://deno.land/x/openai@v4.20.1/mod.ts";

const client = new OpenAI();

const chatCompletion = await client.chat.completions.create({
  messages: [{ role: "user", content: "tell me a joke about dinosaurs" }],
  model: "gpt-4-1106-preview",
});

console.log(chatCompletion);
