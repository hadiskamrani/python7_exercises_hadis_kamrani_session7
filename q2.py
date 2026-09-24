
inventory = {
    "apple": 20,
    "banana": 5,
    "orange": 0,
    "milk": 12,
    "bread": 0
}

def mojodi(inventory):
    list_mojod = []
    list_na_mojod = []
    for key, value in inventory.items():  
        if value != 0:
            list_mojod.append(key)
        if value == 0:    
            list_na_mojod.append(key)
    return list_mojod, list_na_mojod

listemoon = mojodi(inventory)
print(listemoon)





