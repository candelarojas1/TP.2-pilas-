from pila import Stack

# Definir la pila de personajes
personajes = [
    {"nombre": "Iron Man", "peliculas": 10},
    {"nombre": "Captain America", "peliculas": 9},
    {"nombre": "Thor", "peliculas": 8},
    {"nombre": "Black Widow", "peliculas": 7},
    {"nombre": "Hulk", "peliculas": 7},
    {"nombre": "Rocket Raccoon", "peliculas": 4},
    {"nombre": "Groot", "peliculas": 4},
    {"nombre": "Doctor Strange", "peliculas": 3},
    {"nombre": "Spider-Man", "peliculas": 3},
    {"nombre": "Ant-Man", "peliculas": 3},
    {"nombre": "Black Panther", "peliculas": 2},
    {"nombre": "Scarlet Witch", "peliculas": 2},
    {"nombre": "Vision", "peliculas": 2}
]

# Crear una pila para los personajes
pila_personajes = Stack()

# Llenar la pila con los personajes
for personaje in personajes:
    pila_personajes.push(personaje)

# a. Determinar en qué posición se encuentran Rocket Raccoon y Groot
def encontrar_posicion_personaje(pila, nombre_personaje):
    pila_aux = Stack()
    posicion = 1
    encontrado = False

    while pila.size() > 0:
        personaje = pila.pop()
        pila_aux.push(personaje)
        if personaje["nombre"] == nombre_personaje:
            encontrado = True
            break
        posicion += 1

    # Restaurar los elementos a la pila original
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

    if encontrado:
        return posicion
    else:
        return -1  # Indica que el personaje no fue encontrado

posicion_rocket = encontrar_posicion_personaje(pila_personajes, "Rocket Raccoon")
posicion_groot = encontrar_posicion_personaje(pila_personajes, "Groot")

print(f"Rocket Raccoon está en la posición: {posicion_rocket}")
print(f"Groot está en la posición: {posicion_groot}")

# b. Determinar los personajes que participaron en más de 5 películas
def personajes_mas_de_5_peliculas(pila):
    pila_aux = Stack()
    personajes_5_peliculas = []

    while pila.size() > 0:
        personaje = pila.pop()
        if personaje["peliculas"] > 5:
            personajes_5_peliculas.append((personaje["nombre"], personaje["peliculas"]))
        pila_aux.push(personaje)

    # Restaurar los elementos a la pila original
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

    return personajes_5_peliculas

personajes_5_peliculas = personajes_mas_de_5_peliculas(pila_personajes)

print("Personajes que participaron en más de 5 películas:")
for nombre, peliculas in personajes_5_peliculas:
    print(f"{nombre}: {peliculas} películas")

# c. Determinar en cuántas películas participó Black Widow
def peliculas_black_widow(pila):
    pila_aux = Stack()
    peliculas = 0

    while pila.size() > 0:
        personaje = pila.pop()
        if personaje["nombre"] == "Black Widow":
            peliculas = personaje["peliculas"]
        pila_aux.push(personaje)

    # Restaurar los elementos a la pila original
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

    return peliculas

peliculas_viuda_negra = peliculas_black_widow(pila_personajes)
print(f"Black Widow participó en {peliculas_viuda_negra} películas")

# d. Mostrar todos los personajes cuyos nombres empiezan con C, D y G
def personajes_con_letras(pila, letras):
    pila_aux = Stack()
    personajes_filtrados = []

    while pila.size() > 0:
        personaje = pila.pop()
        if personaje["nombre"][0] in letras:
            personajes_filtrados.append(personaje["nombre"])
        pila_aux.push(personaje)

    # Restaurar los elementos a la pila original
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

    return personajes_filtrados

letras = ["C", "D", "G"]
personajes_filtrados = personajes_con_letras(pila_personajes, letras)

print("Personajes cuyos nombres empiezan con C, D y G:")
for nombre in personajes_filtrados:
    print(nombre)
