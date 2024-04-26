"""
11. Comece com o programa que você escreveu no Exercício 4. Crie dois
novos dicionários que representem pessoas diferentes e armazene os três
dicionários em uma lista chamada people . Percorra sua lista de pessoas
com um laço. À medida que percorrer a lista, apresente tudo que você sabe
sobre cada pessoa."""
pessoa1 = {'first_name':'Maria','last_name':'Araujo','age':'18','city':'Brasília'}
pessoa2 = {'first_name':'Isabella','last_name':'Souza','age':'11','city':'Vitória'}
pessoa3 = {'first_name':'Eduardo','last_name':'Silva','age':'35','city':'Goiania'}
people = {}

people = [pessoa1, pessoa2, pessoa3]

for person in people:
    print(f"Nome: {person['first_name']}")
    print(f"Sobrenome: {person['last_name']}")
    print(f"Idade: {person['age']} anos")
    print(f"Cidade: {person['city']}\n")
