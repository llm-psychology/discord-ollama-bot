import asyncio
from ollama import AsyncClient

async def chat():
  message = {'role': 'user', 'content': 'Why is the sky blue?'}
  response = await AsyncClient().chat(model='llama2-uncensored', messages=[message])
  print(response.message.content)

asyncio.run(chat())