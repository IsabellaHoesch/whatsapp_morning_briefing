import news_links as nl
import weather as w
import fun_fact as f
from twilio.rest import Client


#*************************************************************
#config data
# news url:
url_news = "https://www.handelsblatt.com/ticker/"
# wetter url:
url_wetter = "https://www.wetter.com/deutschland/muenchen/DE0006515.html"
# unnützes Wissen url:
url_funf = "https://www.xn--unntzes-wissen-isb.de/site/unnuetzes-Wissen-des-Tages.html"
# Your Account SID from twilio.com/console
account_sid = "AC39ede818a72fbe815e744b01e582d304"
# Your Auth Token from twilio.com/console
auth_token  = "ff02cba22e6dec536508d807e8674842"
# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client(account_sid, auth_token)
# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+491728866377'
contact_directory = {"Isa":'whatsapp:+491728866377'}
                     # "Lexi": "whatsapp:+491726660912",
                     # "Adschie": "whatsapp:+491785258276",
                     # "Milla": "whatsapp:+491734397816",
                     # "Mama": "whatsapp:+491738866377"}
#"Tata":"whatsapp:+491728935975"
#"Josh":"whatsapp:+447909833756"
# "Papa": "whatsapp:+491728370525",

#*************************************************************
for key, value in contact_directory.items():
    client.messages.create(body="Guten Mittag {}!".format(key),
                           from_=from_whatsapp_number,
                           to=value)
#*************************************************************

h_list=nl.gather_headlines(url_news)
h_string='\n\n'.join(h_list)
for key, value in contact_directory.items():
    client.messages.create(body="Todays news:\n" + h_string,
                           from_=from_whatsapp_number,
                           to=value)

#*************************************************************

w_list=w.gather_weather(url_wetter)
w_string='\n\n'.join(w_list)
for key, value in contact_directory.items():
    client.messages.create(body=w_string,
                           from_=from_whatsapp_number,
                           to=value)

#*************************************************************
funfact=f.gather_funfact(url_funf)
for key, value in contact_directory.items():
    client.messages.create(body=funfact,
                           from_=from_whatsapp_number,
                           to=value)

#*************************************************************
for key, value in contact_directory.items():
    client.messages.create(body="Einen wunderschönen Tag wünscht dir Isa!",
                           from_=from_whatsapp_number,
                           to=value)