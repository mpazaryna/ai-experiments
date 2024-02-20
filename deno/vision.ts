import OpenAI from "https://deno.land/x/openai@v4.20.1/mod.ts";

const client = new OpenAI();

const saxroll =
  "https://i1.sndcdn.com/artworks-000025837950-q3jvhm-t240x240.jpg";

const chatCompletion = await client.chat.completions.create({
  model: "gpt-4-vision-preview",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "What’s in this image?" },
        { type: "image_url", image_url: { "url": saxroll } },
      ],
    },
  ],
});

console.log(chatCompletion);
