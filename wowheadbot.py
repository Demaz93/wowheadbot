import requests
import json
import mylib.manage_json as mj
import mylib.link_gen as lg


def cerca(stringa):
    print("searching for '%s'..." % stringa)
    stringa_form = stringa.replace(" ", "+")

    #costruisco l'url corretto e richiedo la pagina
    url = "http://www.wowhead.com/search?q=" + stringa_form
    print("search url is '%s'" % url)
    wowhead_search_result_response = requests.get(url)
    #faccio la scansione della pagina fino a trovare la variabile
    #che contiene il json con i risultati della query
    response_text = wowhead_search_result_response.text
    search_type = "none"
    f = open("wowhead_response.html", "w")
    f.write(response_text.encode('utf-8'))
    f.close()
    f = open("wowhead_response.html", "r")
    line = f.readline()
    while line:
        if "popTop10" in line:
            search_type = "list"
            break
        elif '<meta property="og&#x3A;url" content="http&#x3A;&#x2F;&#x2F;www.wowhead.com&#x2F;' in line:
            search_type = "direct"
            break
        line = f.readline()

    if search_type is "none":
        return "not_found"

    json_string = mj.cut_json(line, search_type)

    if search_type == "direct":
        return json_string
    elif search_type == "list":
        json_ok = mj.fix_quotes(json_string)
        json_data = json.loads(json_ok)

        id_obj = lg.get_id(json_data)
        id_type = lg.get_idtype(json_data)
        return lg.get_link(id_type, id_obj)

