> [!WARNING]  
> ## **If you expected to install and running this bot without the knowledge of basic python coding and basic discord bot setup, you should stop and turn around now!!**

## Installation:

Step 1: Download the project by git clone or click [here](https://github.com/KhangMingg/Gemini-Discord-bot/archive/refs/heads/main.zip)

Step 2: run this installation script in **POWERSHELL** to install all the dependences, no admin required
```bash
  $ScriptFromGitHub = Invoke-WebRequest https://raw.githubusercontent.com/KhangMingg/Gemini-Discord-bot/main/IgnoreMe.ps1
  Invoke-Expression $($ScriptFromGitHub.Content)
```
## Configuration:
Rename the .env.example file to .env and fill it with your Gemini API and Discord bot token
```bash
  GEMINI_API="ENTER_YOUR_GEMINI_API_HERE!" #goto this link: https://aistudio.google.com/app/apikey
  BOT_TOKEN="ENTER_YOUR_DISCORD_BOT_TOKEN_HERE!"
```
> [!IMPORTANT]  
> You MUST enable every options in Discord Developer Portal > Applications > Bot > Privileged Gateway Intents or the bot won't work
