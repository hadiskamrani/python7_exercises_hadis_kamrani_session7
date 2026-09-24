
products = {
    'laptab': 1200,
    'phone': 800,
    'tablet': 500,
    'headphone': 150,
    'mouse': 50
}

def bishtarin_gheymat(products):
    maximum = 0

    for key, value in products.items():
        if value > maximum:
            maximum= value

    return maximum  

balatarin = bishtarin_gheymat(products)
print(balatarin)   




products = {
    'laptab': 1200,
    'phone': 800,
    'tablet': 500,
    'headphone': 150,
    'mouse': 50
}

def name_bishtarin_gheymat(products):
    maximum = 0
    maximum_name = ''

    for key, value in products.items():
        if value > maximum:
            maximum = value
            maximum_name = key  

    return maximum_name

hprice = name_bishtarin_gheymat(products)
print(hprice)   




products = {
    'laptab': 1200,
    'phone': 800,
    'tablet': 500,
    'headphone': 150,
    'mouse': 50
}

def kamtarin_gheymat(products):
    minimum = list(products.values())[0]

    for key, value in products.items():
        if value < minimum:
            minimum = value

    return minimum  

low = kamtarin_gheymat(products)
print(low)   



products = {
    'laptab': 1200,
    'phone': 800,
    'tablet': 500,
    'headphone': 150,
    'mouse': 50
}

def name_kamtarin_gheymat(products):
    minimum = list(products.values())[0]
    minimum_name = ""
    for key, value in products.items():
        if value < minimum:
            minimum = value
            minimum_name = key
    return minimum_name 

lprice = name_kamtarin_gheymat(products)
print(lprice)   




products = {
    'laptab': 1200,
    'phone': 800,
    'tablet': 500,
    'headphone': 150,
    'mouse': 50
}

def jam_kool(products):
    jam = sum(products.values())
    return jam

total = jam_kool(products)
print(total)   



products = {
    'laptab': 1200,
    'phone': 800,
    'tablet': 500,
    'headphone': 150,
    'mouse': 50
}

def miyangin(products):
    count = 0
    for product in products:
        count +=1
    jam = sum(products.values())
    miyangineshoon = jam / count
    return miyangineshoon

average = miyangin(products)
print(average)   








