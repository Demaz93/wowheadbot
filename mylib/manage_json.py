import json
import re


def rep(sjson):
    sjson.replace("\"", "\'")


def fix_quotes(sjson):
    sjson = sjson.replace("\'wowhead\'", "\"wowhead\"") \
        .replace("\'type\'", "\"type\"") \
        .replace("\'typeId\'", "\"typeId\"") \
        .replace("\'lvjson\'", "\"lvjson\"") \
        .replace("searchpopularity", "\"searchpopularity\"") \
        .replace("\'hearthstone\'", "\"hearthstone\"") \
        .replace("undefined", "\"undefined\"")
    return sjson


def cut_json(sjson, stype):
    if stype == "list":
        return sjson[15:-2]
    elif stype == "direct":
        temp1 = sjson[85:-3]
        temp2 = temp1.replace("&#x3D;", "=")
        temp3 = temp2[:temp2.index("&#x2F;")]
        return "http://www.wowhead.com/" + temp3


def print_json(sjson):
    print (json.dumps(sjson, indent=4, sort_keys=True))


def message_ok(sjson):
    return sjson['ok']


def is_empty(sjson):
    if len(sjson['wowhead']) == 0:
        return True
    else:
        return False
