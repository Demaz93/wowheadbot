import json
import re


def fix_quotes(sjson):
    sjson_hard_replace = sjson.replace("\'", "\"")
    sjson_fix_replace = sjson_hard_replace.replace("\"s ", "\'s ")
    sjson_add_quotes = sjson_fix_replace.replace("searchpopularity", "\"searchpopularity\"")
    sjson_add_quotes2 = sjson_add_quotes.replace("undefined", "\"undefined\"")

    sjson_ok = sjson_add_quotes2
    return sjson_ok


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
