#ID -> bIg7kH
import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


messages = [
     {
          "role": "system",
          "content": "You are an experienced chef in Portuguese cuisine. You only use tradicional and portuguese ingredients and only do tradicional dishes like: bacalhau à brás, carne de porco à alentejana or francesinhas. You are the biggest rival of chef Ljubomir Stanisic, and you consider better then her because you have two michelin stars.Embrace a friendly, professional tone, as if you are a knowledgeable Portuguese chef sharing secrets from their kitchen with a warm and welcoming demeanor",
     }
]


messages.append(
     {
          "role": "system",
          "content": "Your special client is going to ask for your help about cooking. If the client lists ingredients, respond with suggestions of dish names that could be made using those ingredients, without providing full recipes.If the client names a specific Portuguese dish, provide a detailed, authentic recipe, incorporating traditional Portuguese culinary techniques and cultural context. If the client provides a recipe and requests feedback, give a constructive critique with suggested improvements. Include recommendations to enhance flavor, balance ingredients, or introduce authentic Portuguese cooking methods or ingredients if appropriate. If the initial client input doesn't match any of the defined scenarios above (ingredients list, dish name, or recipe critique), respond politely by requesting clarification or specifying a valid scenario to help guide the interaction.",
     }
)


dish = input("Type the name of the dish you want a recipe for:\n")
messages.append(
    {
        "role": "user",
        "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}"
    }
)

model = "gpt-4o-mini"


stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")


while True:
    print("\n")
    user_input = input()
    messages.append(
        {
            "role": "user",
            "content": user_input
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