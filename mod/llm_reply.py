from ollama import AsyncClient
from mod.addlog import addlog

async def chat(model_name:str, msg:str)->str:
  addlog.bot.debug("model: "+ model_name) #+號不小心打成逗號 奇怪的bug?????????????
  message = {'role': 'user', 'content': msg, "keep_alive": 0}
  print(msg)
  print(type(msg))
  response = await AsyncClient().chat(model=model_name, messages=[message])
  return (model_name + response.message.content)