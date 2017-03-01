from bs4 import BeautifulSoup
from urllib.request import urlopen
import telegram 

req =  urlopen('https://www.packtpub.com/packt/offers/free-learning')
soup = BeautifulSoup(req, 'html.parser')
title = soup.find('h2').getText()
cover = soup.find('img', class_="imagecache-dotd_main_image")['src']
link = 'https://www.packtpub.com/packt/offers/free-learning'
bot = telegram.Bot(token = 'YOUR_TELEGRAM_BOT_TOKEN')
message = (title.strip() + '\n' + cover[2:].replace(' ', '%20') + '\n' + link )
bot.sendMessage(chat_id="YOUR_CHAT_ID", text = message)


