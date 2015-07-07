def get_idtype(json_data, num_list=0):
    id_type = json_data['wowhead'][int(num_list)]['type']
    print("get_idtype -> %d" % id_type)
    return id_type

def get_id(json_data, num_list=0):
    id = json_data['wowhead'][int(num_list)]['typeId']
    print("get_id -> %d" % id)
    return id

def get_link(id_type, id_obj):
    wowhead_url = "http://www.wowhead.com"
    if id_type == 1:    #npc
        link = wowhead_url + "/npc=" + str(id_obj)
    elif id_type == 3:  #item
        link = wowhead_url + "/item=" + str(id_obj)
    elif id_type == 5:  #quest
        link = wowhead_url + "/quest=" + str(id_obj)
    elif id_type == 6:  #spell
        link = wowhead_url + "/spell=" + str(id_obj)
    elif id_type is 7:  #zone
        link = wowhead_url + "/zone=" + str(id_obj)
    elif id_type == 21: #follower
        link = wowhead_url + "/follower=" + str(id_obj)
    else:
        link = "error" + str(id_type)
    print("get_link %s" % link)
    return link
