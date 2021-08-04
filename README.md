# DisSpy-Public
### NSA Grade Spyware for Discord

## What can it do? 
It can capture all messages that the target recives including group chats and server channels. 
It can also download any media or attachments that are sent to any of the monitored text channels. 
Both auto attachment downloading and server channel logging is disabled by default see **How do I use it?** for more info on how to enable these features.

## Why? 
Because I can, and because there is a lack of spyware for discord. 

## Install
If you don't have git installed then download as a zip and extract it.
navigate to the directory you unziped it to using the `cd <folderName>` command then run `pip3 install -r requirements.txt`
TIP: If your on windows, open the folder then click the folder path, and type `cmd.exe`
Afterwards run `python3 DisSpyV1.py`

Alternatively you can run `git clone https://github.com/OMN1-H1V3/DisSpy-Public.git` 
`cd DisSpy-Public` 
`pip3 install -r requirements.txt`
`python3 DisSpyV1.py`

## How do I use it?
Just run it and when prompted provide your target's token. 

Server channel logging is disabled by default, you will need to enable it by changing `capServers = False` to `capServers = True` if you want to log messages sent in server channels.

This is disabled by default, you will need to enable it by changing `downloadMedia = False` to `downloadMedia = True` if you want to auto-download attachments.

(If you want to enable/disable server message logging or attachment downloading edit `DisSpyV1.py` first before you run it)

## Bug Reports
I'll try and matain this often but it should be basically done. If you encounter a bug just make an issue and ill check it out.

### Credits
Started as a bug fix for [discord.spy](https://github.com/spicesouls/discord.spy), ended up fixing it and adding support for servers and group chats and file downloads.



#### I take 0 responsibility for how you use this tool. This is for educational purposes only.
##### This is a selfbot, which is against discords TOS, the accounts that are used within this tool are technically running a selfbot, meaning they could be banned.
