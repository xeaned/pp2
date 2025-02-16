import json

with open("/Users/rapiyatleukhan/Desktop/pp2/lab4/JSON/sample-data.json", "r") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 90)
print(f"{'DN':50} {'Description':20} {'Speed':7} {'MTU'}")
print("-" * 90)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "")
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")
    print(f"{dn:50} {descr:20} {speed:8} {mtu}")