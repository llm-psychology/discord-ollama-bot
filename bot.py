#auto py to exe ->Manual Argument Input-> --collect-data grapheme

import discord
from discord.ext import commands,tasks
import os
from mod.environment_variables import init 
from mod.addlog import addlog
from mod.message_process import message_process
import sys

print(sys.version_info) #顯示python的版本

#ctx: commands.context.Context
#不可以ctx: discord.ext.commands.context.Context
#ctx是discord目錄下的一個資料夾 沒有寫在init裡面
VERSION = "3.0"
ID,TOKEN,SERVERWEBHOOK,BOTWEBHOOK,MORNING = init()
counter_for_MOTD = 0

#--------------------------------------------------------------------------------------------
    
class Lijiu_bot(commands.Bot): #繼承bot
    def __init__(self) -> None:
        intents = discord.Intents.all()
        intents.message_content = True #v2
        intents.members = True
        super().__init__(command_prefix=commands.when_mentioned_or(','), intents=intents)
        
#--------------------------------------------------------------------------------------------
bot = Lijiu_bot()
#--------------------------------------------------------------------------------------------


@bot.event
async def on_ready():
    addlog.bot.info(">>>>>>>>>已上線<<<<<<<<<")
    addlog.bot.info('目前登入身份：' + os.getlogin() + ":" + str(bot.user))
    if not check_loop.is_running():
        check_loop.start() 
    


@tasks.loop(hours=1)
async def check_loop():
    addlog.server.info("上線中")
    
@bot.event
async def on_message(message: discord.message.Message):
    
    if message.author.bot: #排除掉機器人、自己還有webhook傳的訊息
        return
    
    #加了這行才可以監聽on_message順便還有指令的功能，要不然一開始on_message會override bot的command權限
    await bot.process_commands(message)  
    await message_process.message_process(message,bot)

 #--------------------------------------------------------------------------------------------

if __name__ == "__main__":
    bot.run(TOKEN) 
 #--------------------------------------------------------------------------------------------
