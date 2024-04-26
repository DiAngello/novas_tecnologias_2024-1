"""
12. Crie vários dicionários, em que o nome de cada dicionário seja o nome de
um animal de estimação. Em cada dicionário, inclua o tipo do animal e o
nome do dono. Armazene esses dicionários em uma lista chamada pets .
Em seguida, percorra sua lista com um laço e, à medida que fizer isso,
apresente tudo que você sabe sobre cada animal de estimação.
"""
lua = {'nome': 'Lua', 'tipo': 'gato', 'dono': 'Maria'}
bob = {'nome': 'Bob', 'tipo': 'cachorro', 'dono': 'Isabela'}
clara = {'nome': 'Clara', 'tipo': 'pássaro', 'dono': 'Eduardo'}

pets = [lua, bob, clara]

for pet in pets:
    print(f"{pet['nome']} ")
    print(f"tipo: {pet['tipo']} ")
    print(f"dono: {pet['dono']}\n")
