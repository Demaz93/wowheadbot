import urllib
import json
import re
from bs4 import BeautifulSoup


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

#aggiusto la stringa in modo che venga riconosciuta correttamente come json
json_string = line[15:-2]
json_string2 = json_string.replace("\'","\"")
json_string3 = json_string2.replace("\"s ","\'s ")
json_string4 = json_string3.replace("searchpopularity","\"searchpopularity\"")
json_string5 = json_string4.replace("undefined","\"undefined\"")

print json_string5

json_data = json.loads(json_string5)

#print json.dumps(json_data['wowhead'],indent=6,sort_keys=True)
#print json_data['wowhead']

#prendo il tipo e l'id del primo risultato
tipo = json_data['wowhead'][0]['type']
id_obj = json_data['wowhead'][0]['lvjson']['id']

if tipo == 1:
    print "http://www.wowhead.com/npc=" + str(id_obj)
elif tipo == 2:
    print "boh 2"
elif tipo == 3:
    print "http://www.wowhead.com/item=" + str(id_obj)
elif tipo == 4:
    print "boh 4"
elif tipo == 5:
    print "http://www.wowhead.com/quest=" + str(id_obj)
elif tipo == 6:
    print "http://www.wowhead.com/spell=" + str(id_obj)
elif tipo == 21:
    print "http://www.wowhead.com/follower=" + str(id_obj)
else:
    print "errore" + str(tipo)



#npc = 1
#item = 3
#spell = 6
