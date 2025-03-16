import json

with open("/Users/rapiyatleukhan/Desktop/pp2/lab4/JSON/easy_sample.json", "r") as file:
    data = json.load(file)  # JSON -> Python


data["age"] = 3  # Обновляем существующий ключ
data["city"] = "Almaty"  # Добавляем новый ключ


print(json.dumps(data, indent=4))  

with open("/Users/rapiyatleukhan/Desktop/pp2/lab4/JSON/easy_sample.json", "w") as file:
    json.dump(data, file, indent=4)  # Python -> JSON




    import re

def extract_vowels(text):
    return ''.join(filter(lambda char: re.match(r'[аеёиоуыэюяАЕЁИОУЫЭЮЯ]', char), text))

text = "Привет, как дела?"
vowels = extract_vowels(text)
print(vowels)