from pila import Stack

# Personajes del episodio V "The Empire Strikes Back"
personajes_episodio_v = ["Luke Skywalker", "Princess Leia", "Han Solo", "Darth Vader", "Yoda"]

# Personajes del episodio VII "The Force Awakens"
personajes_episodio_vii = ["Luke Skywalker", "Rey", "Han Solo", "Kylo Ren", "Finn"]

# Crear pilas para los personajes de cada episodio
pila_episodio_v = Stack()
pila_episodio_vii = Stack()

# Llenar las pilas con los personajes respectivos
for personaje in personajes_episodio_v:
    pila_episodio_v.push(personaje)

for personaje in personajes_episodio_vii:
    pila_episodio_vii.push(personaje)

# Crear una tercera pila para la intersección de personajes
interseccion_pilas = Stack()

# Iterar sobre la pila del episodio V y verificar si cada personaje está en la pila del episodio VII
while pila_episodio_v.size() > 0:
    personaje_v = pila_episodio_v.pop()
    if personaje_v in personajes_episodio_vii:
        interseccion_pilas.push(personaje_v)

# Mostrar los personajes que aparecen en ambos episodios
print("Personajes que aparecen en ambos episodios:")
while interseccion_pilas.size() > 0:
    print(interseccion_pilas.pop())