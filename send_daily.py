import config as conf
import news_links as nl
import weather as w
import fun_fact as f
from twilio.rest import Client

#*************************************************************
# Twilio sandbox number from which messages are sent
from_whatsapp_nr = conf.from_whatsapp_number
# Contact directory to whom messages are being sent
contact_dir = conf.contact_directory



client = Client()

#*************************************************************
for key, value in contact_dir.items():
    client.messages.create(body="Guten Mittag {}!".format(key),
                           from_=from_whatsapp_nr,
                           to=value)
#*************************************************************

h_list=nl.gather_headlines()
h_string='\n\n'.join(h_list)
for key, value in contact_dir.items():
    client.messages.create(body="Todays news:\n" + h_string,
                           from_=from_whatsapp_nr,
                           to=value)

#*************************************************************

w_list=w.gather_weather()
w_string='\n\n'.join(w_list)
for key, value in contact_dir.items():
    client.messages.create(body=w_string,
                           from_=from_whatsapp_nr,
                           to=value)

#*************************************************************
funfact=f.gather_funfact()
for key, value in contact_dir.items():
    client.messages.create(body=funfact,
                           from_=from_whatsapp_nr,
                           to=value)

#*************************************************************
for key, value in contact_dir.items():
    client.messages.create(body="Einen wunderschönen Tag wünscht dir Isa!",
                           from_=from_whatsapp_nr,
                           to=value)