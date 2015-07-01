def get_idtype(json_data, num_list=0):
    return json_data['wowhead'][int(num_list)]['type']

def get_id(json_data, num_list=0):
    return json_data['wowhead'][int(num_list)]['typeId']

def get_link(id_type, id_obj):
    if id_type == 1:    #npc
        return "http://www.wowhead.com/npc=" + str(id_obj)
    elif id_type == 3:  #item
        return "http://www.wowhead.com/item=" + str(id_obj)
    elif id_type == 5:  #quest
        return "http://www.wowhead.com/quest=" + str(id_obj)
    elif id_type == 6:  #spell
        return "http://www.wowhead.com/spell=" + str(id_obj)
    elif id_type == 21: #follower
        return "http://www.wowhead.com/follower=" + str(id_obj)
    else:
        return "error" + str(id_type)
