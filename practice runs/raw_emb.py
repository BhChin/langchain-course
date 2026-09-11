import os

from dotenv import load_dotenv
from anthropic import Anthropic
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

conversation = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
    ],
)

#print(conversation.choices[0].message.content)

response = client.embeddings.create(
    input="Your text string goes here", model="text-embedding-3-small"
)

print(response)
print(len(response.data[0].embedding)) #dimension of our embedding
#embedding models have different dimensions
#the more dimensions = more context/features the embedding can have


# client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
#
# message = client.messages.create(
#     model="claude-sonnet-5",
#     max_tokens=1024,
#     system="You are a helpful assistant.",
#     messages=[
#         {"role": "user", "content": "What is the capital of France?"},
#     ],
# )

#print(message.content[0].text)

#anthropic doesn't have their own embedding models

