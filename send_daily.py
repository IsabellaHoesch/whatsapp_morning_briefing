"""
Main file
"""

import config as conf
import news_links as nl
import weather as w
import fun_fact as f
from twilio.rest import Client
#*************************************************************

from_whatsapp_nr = conf.from_whatsapp_number  # Twilio sandbox number from which messages are sent
contact_dir = conf.contact_directory # Contact directory to whom messages are being sent

#*************************************************************
client = Client()
for key, value in contact_dir.items():
# Greeting Good-morning
    client.messages.create(body="Guten Nachmittag {}!".format(key),
                           from_=from_whatsapp_nr,
                           to=value)
# News headlines
    client.messages.create(body="Todays news:\n" + nl.gather_headlines(),
                           from_=from_whatsapp_nr,
                           to=value)
# Weather
    client.messages.create(body=w.gather_weather(),
                           from_=from_whatsapp_nr,
                           to=value)
# Funfact
    client.messages.create(body=f.gather_funfact(),
                           from_=from_whatsapp_nr,
                           to=value)
# Greeting good-bye
    client.messages.create(body="Einen wunderschönen Tag wünscht dir Isa!",
                           from_=from_whatsapp_nr,
                           to=value)
