__author__ = 'Matteo De Marie'

import sys
import requests
import json
import mylib.manage_json as mj
import wowheadbot as bot
import time
import traceback
import telebot


def extract_token(filename):
    t = open(filename, "r")
    token = t.readline()
    print("token is %s" % token)
    return token


def listener(*messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            text = m.text
            search_result = search_wowhead(text)
            tb.send_message(chatid, search_result)


def search_wowhead(search_string):
    try:
        search = search_string.replace("/wowhead ", "")
        message = bot.search(search)
    except Exception as e:
        message = "exception '%s'" % e.message
        traceback.print_exc()
    return message


token = extract_token("key.token")
tb = telebot.TeleBot(token)
tb.set_update_listener(listener)
tb.polling()

while True:
    pass

#if __name__ == '__main__':
    #main()