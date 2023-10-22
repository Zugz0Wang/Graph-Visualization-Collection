indices = []

def parent(i):
    return int((i + 1) / 2 - 1)

for i in range(1, 1024):
    indices.append(parent(i))
    indices.append(i)

import json

json.dump({"indices": indices}, open("BT/BT.graph.json", 'w'))