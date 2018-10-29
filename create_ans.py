import json

hosts = []
with open("sat.json") as x:
    data = json.load(x)
    x.close()
    result = data.get("results")

    for i in range(len(data.get("results"))):
        hosts.append((result[i].get("default_organization").get("name")))

    print (hosts)

