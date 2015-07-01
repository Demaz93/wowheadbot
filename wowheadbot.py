import urllib
import json
from mylib.manage_json import *
from mylib.link_gen import *

stringa = "savage blood"
#sistemo la stringa in modo che venga accettata dalla query
#sostituendo gli spazzi con il +

stringa_form = stringa.replace(" ","+")

#costruisco l'url corretto e richiedo la pagina
url = "http://www.wowhead.com/search?q=" + stringa_form
urlok = urllib.urlopen(url)

#faccio la scansione della pagina fino a trovare la variabile
#che contiene il json con i risultati della query
line = urlok.readline()
while line:
    line = urlok.readline()
    if "popTop10" not in line: continue
    else:
        break
        
json_string = cut_json(line)
json_ok = fix_quotes(json_string)

json_data = json.loads(json_ok)

id_obj = get_id(json_data)
id_type = get_idtype(json_data)

print get_link(id_type, id_obj)
