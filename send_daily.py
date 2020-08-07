"""
Main file that is run to send scraped information using twilio
"""

import config as conf
import web_info as w
from twilio.rest import Client
#*************************************************************

from_whatsapp_nr = conf.from_whatsapp_number  # Sender: Twilio sandbox number from which messages are sent
contact_dir = conf.contact_directory  # Recipients: Contact directory to whom messages are being sent

#*************************************************************
if __name__ == "__main__":
    client = Client() # this requires a authorization key and token that is retrived from twilio sandbox and stored as a path variable
    for key, value in contact_dir.items():
    # Greeting Good-morning
        client.messages.create(body="Guten Morgen {}!".format(key),
                               from_=from_whatsapp_nr,
                               to=value)
    # News headlines
        client.messages.create(body="Todays news:\n" + w.gather_headlines(),
                               from_=from_whatsapp_nr,
                               to=value)
    # Weather
        client.messages.create(body=w.gather_weather(),
                               from_=from_whatsapp_nr,
                               to=value)
    # Funfact
        client.messages.create(body=w.gather_funfact(),
                               from_=from_whatsapp_nr,
                               to=value)
    # Greeting good-bye
        client.messages.create(body="Einen wunderschönen Tag wünscht dir Isa!",
                               from_=from_whatsapp_nr,
                               to=value)



