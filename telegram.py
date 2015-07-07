__author__ = 'Matteo De Marie'

import sys
import requests
import json
import mylib.manage_json as mj
import wowheadbot as bot
import time
import traceback

def main():
    token = extract_token("key.token")
    get_updates_response = requests.get("https://api.telegram.org/bot" + token + "/getupdates")

    if get_updates_response.status_code is 200:
        json_data = json.loads(get_updates_response.text)
        json.dump(json_data, sys.stdout, sort_keys=True, indent=4, separators=(',', ': '))
        print(json_data)
        get_updates_response.close()  # non usare piu' get_updates_response
        check_for_updates(token)


def extract_token(filename):
    t = open(filename, "r")
    token = t.readline()
    return token


def check_for_updates(token):
    with open("last_id", "r") as f:
        last_id = f.readline()

    while True:
        time.sleep(2)  # non riempire di richieste il server
        get_updates_request = "https://api.telegram.org/bot" + token + "/getupdates?offset=" + str(last_id)
        json_data = json.loads(requests.get(get_updates_request).text)

        if len(json_data['result']) != 1 and mj.message_ok(json_data):
            for i in range(1, len(json_data['result'])):
                if "/wowhead" in json_data['result'][i]['message']['text']:
                    comando = json_data['result'][i]['message']['text']
                    ssearch = comando.replace("/wowhead ", "")

                    chat_id = json_data['result'][i]['message']['chat']['id']
                    try:
                        message = bot.cerca(ssearch)
                    except Exception as e:
                        message = "exception '%s'" % e.message
                        traceback.print_exc()

                    send_message_request = "https://api.telegram.org/bot" + token + "/sendmessage?chat_id=" + str(
                        chat_id) + "&text=" + message

                    print (send_message_request)
                    requests.post(send_message_request)

            last_id = json_data['result'][len(json_data['result']) - 1]['update_id']
            with open("last_id", "w") as f:
                f.write(str(last_id))


if __name__ == '__main__':
    main()