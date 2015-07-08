__author__ = 'Matteo De Marie'

import traceback

import telebot

import wowheadbot as bot


tb = None


def extract_token(filename):
    t = open(filename, "r")
    token = t.readline()
    print("token is %s" % token)
    return token


def listener(*messages):
    # When new messages arrive TeleBot will call this function.
    for m in messages:
        msg = m[0]  # dio can, coglione di telebot
        chat_id = msg.chat.id
        if msg.content_type == 'text':
            search_result = search_wowhead(msg.text)
            tb.send_message(chat_id, search_result)


def search_wowhead(search_string):
    try:
        search = search_string.replace("/wowhead ", "")
        message = bot.search(search)
    except Exception as e:
        message = "exception '%s'" % e.message
        traceback.print_exc()
    return message


def main():
    token = extract_token("key.token")
    global tb
    tb = telebot.TeleBot(token)
    tb.set_update_listener(listener)
    tb.polling()

    while True:
        pass


if __name__ == '__main__':
    main()