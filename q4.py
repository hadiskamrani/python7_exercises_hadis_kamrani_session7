sales = (
    ("Ali", "Laptop", 1200),
    ("Sara", "Phone", 800),
    ("Ali", "Phone", 800),
    ("Reza", "Laptop", 1200),
    ("Sara", "Laptop", 1200),
    ("Ali", "Mouse", 50)
)
def kharid_afrad(sales):
    natije = {}
    for name, product, price in sales:
        if name in natije:
            natije[name] = natije[name] + price   
        else:
            natije[name] = price               
    return natije


print(kharid_afrad(sales))



sales = (
    ("Ali", "Laptop", 1200),
    ("Sara", "Phone", 800),
    ("Ali", "Phone", 800),
    ("Reza", "Laptop", 1200),
    ("Sara", "Laptop", 1200),
    ("Ali", "Mouse", 50)
)



def tedad_forosh(sales):
    natije = {}
    for name, product, price in sales:
        if product in natije:
            natije[product] = natije[product] + 1
        else:
            natije[product] = 1
    return natije


print(tedad_forosh(sales))



sales = (
    ("Ali", "Laptop", 1200),
    ("Sara", "Phone", 800),
    ("Ali", "Phone", 800),
    ("Reza", "Laptop", 1200),
    ("Sara", "Laptop", 1200),
    ("Ali", "Mouse", 50)
)





def daramad_kol(sales):
    majmoo = 0
    for name, product, price in sales:
        majmoo = majmoo + price
    return majmoo


print(daramad_kol(sales))