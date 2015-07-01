import urllib
import json
import mylib.manage_json
import mylib.link_gen

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
        
json_string = mylib.manage_json.cut_json(line)
json_ok = mylib.manage_json.fix_quotes(json_string)

json_data = json.loads(json_ok)

id_obj = mylib.link_gen.get_id(json_data)
id_type = mylib.link_gen.get_idtype(json_data)

print mylib.link_gen.get_link(id_type, id_obj)
