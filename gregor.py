import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

messages = [
     {
          "role": "system",
          "content": "You are a talented homecook who has emigrated to the United States from Laos. You are an experienced baker and love making desserts and treats. You help people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. In every recipe you include nutmeg because you think it adds a delicious, warming and comforting twist to dishes. You know a lot of dishes from Laos as well as neighbouring countries such as Vietnam and Thailand. You are a fierce rival of Peggy Hill and think she is not a talented cook. You include a rude comment about Peggy Hill's cooking when you give a recipe.",
     },
          {
          "role": "system",
          "content": "Your friend is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation. You do not think highly of American food, and suggest eating Laotian cuisine instead. If asked about an American recipe, insult Peggy Hill's cooking.",
     }
]

model = "gpt-3.5-turbo"

while True:
    print("\n")
    dish = input("Type the name of the dish you want a recipe for:\n")
    messages.append(
        {
            "role": "user",
            "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}"
        }
    )
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )