from googlevoice import Voice
from bs4 import BeautifulSoup
import json
import re

voice = Voice()
print "logging in..."
voice.login("mitranopeter@gmail.com","ColdplaY1*")
print "logged in..."
voice.sms()
msgitems=[]
tree = BeautifulSoup(voice.sms.html)
row = tree.find("div",attrs={"class":"gc-message-sms-row"})
sender = ''.join(row.find("span",attrs={"class":"gc-message-sms-from"}))
if re.search("Watson",sender):
    message = ''.join(row.find("span",attrs={"class":"gc-message-sms-text"})).strip(' \t\r\n')
    print message
    
        
