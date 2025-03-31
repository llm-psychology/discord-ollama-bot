from mod.addlog import addlog
from mod.llm_reply import chat


MODEL = ["llama2-uncensored", "dolphin-llama3:latest",
        "qwen2.5:32b", "deepseek-r1",
         "phi4", "llama3.2-vision", "deepseek-r1"]

class message_process:
    async def message_process(message,bot):
        #log to main server
        addlog.bot.debug(" "+ str(message.author) + "/" +str(message.guild.name) + " : " + str(message.channel) + " : " + str(message.content))
        
        if str(message.channel) == "機器人log" or str(message.channel) == "llm測試-bot":
            #TODO: check Vram available size
            #llm_reply
            for i, model_name in enumerate(MODEL):
                llm_responds = await chat(model_name, str(message.content))
                await message.channel.send(llm_responds)
    
'''NAME                            ID              SIZE      MODIFIED
llama2-uncensored:latest        44040b922233    3.8 GB    49 minutes ago
dolphin-llama3:latest           613f068e29f8    4.7 GB    4 weeks ago
wizard-vicuna-uncensored:30b    5a7102e25304    18 GB     4 weeks ago
openthinker:32b                 b3f4e577e166    19 GB     4 weeks ago
llama2-uncensored:7b            44040b922233    3.8 GB    4 weeks ago
deepseek-coder-v2:latest        63fb193b3a9b    8.9 GB    4 weeks ago
qwen2.5-coder:32b               4bd6cbf2d094    19 GB     4 weeks ago
qwen2.5:32b                     9f13ba1299af    19 GB     4 weeks ago
deepseek-r1:14b                 ea35dfe18182    9.0 GB    4 weeks ago
gemma2:27b                      53261bc9c192    15 GB     4 weeks ago
phi4:latest                     ac896e5b8b34    9.1 GB    4 weeks ago
llama3.2-vision:latest          085a1fdae525    7.9 GB    4 weeks ago
deepseek-r1:latest              0a8c26691023    4.7 GB    4 weeks ago'''