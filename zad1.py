import json

data = json.load(
    open("simple.json")
    )

# print(type(data))
# print(data['imie'][0])

print(f'DANE Z PLIKU to:\n{data}')