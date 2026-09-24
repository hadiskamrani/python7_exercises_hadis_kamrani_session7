employees = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },

    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },

    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
}


def balatarin_hoghoogh(employees):
    bishtarin_hoghoogh = 0
    name = ""

    for key, value in employees.items():
        hoghoogh = value["salary"]
        if hoghoogh > bishtarin_hoghoogh:
            bishtarin_hoghoogh = hoghoogh
            name = value["name"]  

    return name

high_income = balatarin_hoghoogh(employees)
print(high_income)



employees = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },

    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },

    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
}


def kamtarin_hoghoogh(employees):
    first = list(employees.values())[0]
    kamtarin_hoghoogh = first["salary"]
    name = first["name"]

    for key, value in employees.items():
        if value["salary"] < kamtarin_hoghoogh:
            kamtarin_hoghoogh = value["salary"]
            name = value["name"]

    return name


print(kamtarin_hoghoogh(employees))   



employees = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },

    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },

    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
}

def list_afrad(employees):
    listemoon = []
    for key, value in employees.items():
        if value["salary"] >= 3000:
            listemoon.append(value["name"])
    return listemoon


print(list_afrad(employees))



employees = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },

    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },

    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
}

def hoghogh(employees,number):
    listte_afrad=[]
    for key,value in employees.items():
        if value["salary"] > number:
            listte_afrad.append(value["name"])
    return listte_afrad

print(hoghogh(employees, 2900))
            
    
    
employees = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },

    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },

    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
}

def miyangin(employees):
    count = 0
    majmoo = 0                    
    for value in employees.values():
        count = count + 1
        majmoo = majmoo + value["salary"]    
    average = majmoo / count      
    return average

print(miyangin(employees))
    
    


