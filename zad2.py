import json

data = json.load(
open("simple.json")
    )

word = input('Podaj slowo-klucz: ')

result = data[word]

print(f'Wartość to:\n{result}')