people = [
    {"name": "Saitama", "house": "Carece de capa"},
    {"name": "Goku", "house": "Saiyajin"},
    {"name": "Vegeta", "house": "Saiyajin"}
]

# def f(person):
#    return person["house"]

# Sem utilizar a função acima, em apenas uma linha
people.sort(key = lambda person: person["name"])
print(people)

