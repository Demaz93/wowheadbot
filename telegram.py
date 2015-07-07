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
        json.dump(json_data, sys.stdout, indent=4, separators=(',', ': '))
        print('\n')
        get_updates_response.close()  # non usare piu' get_updates_response
        check_for_updates(token)


def extract_token(filename):
    t = open(filename, "r")
    token = t.readline()
    print("token is %s" % token)
    return token


def check_for_updates(token):
    with open("last_id", "r") as f:
        last_id = f.readline()
        print("last request id is %s" % last_id)

    while True:
        time.sleep(2)  # non riempire di richieste il server
        get_updates_request = "https://api.telegram.org/bot" + token + "/getupdates?offset=" + str(last_id)
        get_updates_response = requests.get(get_updates_request)
        json_data = json.loads(get_updates_response.text)
        get_updates_response.close()

        if len(json_data['result']) != 1 and mj.message_ok(json_data):
            json.dump(json_data, sys.stdout, indent=4, separators=(',', ': '))
            print('\n')
            for i in range(1, len(json_data['result'])):
                if "/wowhead" in json_data['result'][i]['message']['text']:
                    command = json_data['result'][i]['message']['text']
                    search_string = command.replace("/wowhead ", "")

                    chat_id = json_data['result'][i]['message']['chat']['id']
                    try:
                        message = bot.search(search_string)
                    except Exception as e:
                        message = "exception '%s'" % e.message
                        traceback.print_exc()

                    send_message_request = "https://api.telegram.org/bot" + token + "/sendmessage?chat_id=" + str(
                        chat_id) + "&text=" + message

                    print (send_message_request)
                    message_post = requests.post(send_message_request)
                    message_post.close()

            try:
                last_id = json_data['result'][len(json_data['result']) - 1]['update_id']
                with open("last_id", "w") as f:
                    f.write(str(last_id))
            except IndexError as e:
                print(e)


if __name__ == '__main__':
    main()