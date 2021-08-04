# DisSpy-Public
### NSA Grade Spyware for Discord

## What can it do? 
It can capture all messages that the target recives including group chats and server channels. 
Server channel logging is disabled by default, you will need to enable it by changing ``capServers = False`` to ``capServers = True``.

It can also download any media or attachments that are sent to any of the monitored text channels. 
This is disabled by default, you will need to enable it by changing ``downloadMedia = False`` to ``downloadMedia = True`` 

## Why? 
Because I can, and because there is a lack of spyware for discord. 

## How do I use it?
Well, you should probably learn how to use a python script, then install the imports, then once you have done that you can run it.
Wouldn't recommend using on windows unless you change line 9 from `` os.system("clear")`` to `` os.system("cls")`` as it will throw an error because I couldn't be bothered to add a smart screen clear.

### Credits
Started as a bug fix for [discord.spy](https://github.com/spicesouls/discord.spy), ended up fixing it and adding support for servers and group chats and file downloads.





#### I take 0 responsibility for how you use this tool. This is for educational purposes only.
##### This is a selfbot, which is against discords TOS, the accounts that are used within this tool are technically running a selfbot, meaning they could be banned.
