# PackPubFree Bot

### Small script to parse newest "packpub free learning" books offert and send via Telegram on group chat or bot chat.

## Install

Installation is realy simple. Create Telegram Bot using BotFather on Telegram. 
Create group chat or channel and add bot to it. If you are not familiar with Telegram bot API, read the docs.
https://core.telegram.org/bots

## Setings

* Telegram bot token

Set your private telegram bot token.

```python
bot = telegram.Bot(token = 'YOUR_TELEGRAM_BOT_TOKEN')
``` 

* Telegram chat_id 
Set Telegram channel id for posting
```python
bot.sendMessage(chat_id="YOUR_CHAT_ID", text = message)
```
## Summary

Offerts on packpub free learing, are updated once a day, so there is no need to execute script (manualy or cron) more often.
