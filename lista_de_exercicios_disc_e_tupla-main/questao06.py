# 6) Escreva uma função que conta a quantidade de vowels em um texto e
# armazena tal quantidade em um dicionário, onde a chave é a vogal
# considerada.

def count_vowels(texto):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letter in texto:
        if letter.lower() in vowels:
            vowels[letter.lower()] += 1
    return vowels

text = input('Informe um texto para suas vogais serem contadas: ')
result = count_vowels(text)
print(result)