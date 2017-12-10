import json

with open('ganadores.json', 'r') as file:
    data = json.load(file)

data = {
    'ganadores' : input("ingrese su nombre: ")

}

with open('ganadores.json', 'w') as file:
    json.dump(data, file)