import json

def niveles(nivel):
    with open('mapa.json', 'r') as file:
        data = json.load(file)
        mapa = data['niveles']

    return mapa[nivel]


