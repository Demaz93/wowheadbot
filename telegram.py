__author__ = 'Matteo De Marie'

import urllib.request as urlr
import json
import mylib.manage_json as mj
import wowheadbot as bot
import time

t = open("key.token", "r")
token = t.readline()
last_id = 0

url1 = "https://api.telegram.org/bot" + token + "/getupdates"
urlok1 = urlr.urlopen(url1)
line1 = urlok1.read().decode('utf8')
json_data = json.loads(line1)

while 1:
    time.sleep(2)
    url = "https://api.telegram.org/bot" + token + "/getupdates?offset=" + str(last_id)
    #print (url)
    urlok = urlr.urlopen(url)
    line = urlok.read().decode('utf8')
    json_data = json.loads(line)

    if len(json_data['result']) != 1:
        if mj.message_ok(json_data):
            for i in range(1, len(json_data['result'])):
                if "/wowhead" in json_data['result'][i]['message']['text']:
                    comando = json_data['result'][i]['message']['text']
                    ssearch = comando.replace("/wowhead ","")

                    chat_id = json_data['result'][i]['message']['chat']['id']
                    message = bot.cerca(ssearch)
                    url_msg = "https://api.telegram.org/bot" + token + "/sendmessage?chat_id=" + str(chat_id) + "&text=" + message
                    print (url_msg)
                    urlr.urlopen(url_msg)

            last_id = json_data['result'][len(json_data['result'])-1]['update_id']

