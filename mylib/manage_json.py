import json

def fix_quotes(sjson):
    sjson_hard_replace = sjson.replace("\'","\"")
    sjson_fix_replace = sjson_hard_replace.replace("\"s ","\'s ")
    sjson_add_quotes = sjson_fix_replace.replace("searchpopularity","\"searchpopularity\"")
    sjson_add_quotes2 = sjson_add_quotes.replace("undefined","\"undefined\"")
    
    sjson_ok = sjson_add_quotes2
    return sjson_ok
    
def cut_json(sjson):
    return sjson[15:-2]

def print_json(sjson):
    print json.dumps(sjson,indent=4,sort_keys=True)

