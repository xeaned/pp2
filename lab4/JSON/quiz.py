import json 

with open("/Users/rapiyatleukhan/Desktop/pp2/lab4/JSON/sample.json", "r") as file:
    data = json.load(file)

data["price"]=900

print(json.dumps(data))  

with open("/Users/rapiyatleukhan/Desktop/pp2/lab4/JSON/sample.json", "w") as file:
    json.dump(data, file)