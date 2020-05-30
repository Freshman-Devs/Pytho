This is the guide you need to read to get your Python bot up and running.

Requirements:
Python 3.8 or higher
Code Editer (recommended, but you can just use notepad)

// Hosting
You can just host it on your computer, but it is recommended to use a VPS or Raspberry Pi.

We recommend a Raspberry Pi. (They come pre-installed with Python). Buy one from here:
https://www.amazon.com/CanaKit-Raspberry-Wireless-Complete-Starter/dp/B072N3X39J/ref=sr_1_2?dchild=1&keywords=Raspberry+Pi+Zero+W&qid=1590867722&sr=8-2

Otherwise, we would recommend these VPS services:
Microsoft Azure
Google Cloud
Amazon EC2
Amazon Lightsail

// Making an application

To do this, login to your Discord account on your browser. Then, go to https://discord.com/developers/.
Create a new application, and name it what you want. (Please don't use the name Pytho or use Pytho's icon).
If you would like, add a profile picture to the bot.

// Making a bot user

After you have done all that, head over to the Bot tab from the menu. Create a bot, and copy the token.

// Setting up our bot to use the bot user we just created
Open the bot.py file in a code editor (notepad works fine if you don't have a code editor). Find TOKEN = 'YOUR TOKEN HERE' in bot.py.
Remove YOUR TOKEN here and replace it with your token.

Next, find this in bot.py:

@client.event
async def on_ready():
    print('Ready!')
    activity = discord.Game(name="whatever you want", type=0)
    await client.change_presence(status=discord.Status.online, activity=activity)
    
    Replace whatever you want with the status you want your bot to have. (Note: It will be a Playing status, not a custom status.)
    
 Now, open a terminal. Type the following command:
 
 For Windows:
 py -3 -m pip install -U discord.py
 
 For macOS and Linux:
 
 python3 -m pip install -U discord.py
 
 // Running your bot
 
 Running it on your PC:
 This isn't recommended because it will only be online while we are running the python script on your PC, but you can.
 Open your bots folder in a terminal, and type the following command:
 
 Windows: 
 python bot.py
 
 Mac, Linux and Raspbian: python3 bot.py
 
 // Inviting your bot
 
 A bot is basically useless if you can't invite it to any servers. SO here is how to invite your bot to servers!
 
 Open up your bot in Discord Developer Portal (discord.com/developers) and click the OAuth2 tab.
 Check the bot scope, then scroll all the way down and click Administrator.
 Copy the invite link and paste it in your browser, and invite it to your server!
 
 And that is it. You now have a working discord bot! If you have any issues, feel free to contact the dev team in our discord server! (https://discord.gg/rPAyzNs0)

 
 
    
    
    
