import json

input_path = './clusters.json'
with open(input_path) as fp:
    old_data = json.load(fp)
node_map = {}
l = len(old_data[-1])
for x in range(0, l):
    node_map[x] = {"name": str(x), "size": old_data[-1][x]}
count = len(old_data[0])
for y in range(0, count):
    cur_group = old_data[1][y]
    cur_len = len(cur_group)
    cur_map = {"name":"", "children":[]}
    for z in range(0, cur_len):
        if len(cur_group[z]) == 1:
            cur_map["children"].append(node_map[cur_group[z][0]])
        else:
            temp_map = {"name": "", "children": []}
            for n in range(0, len(cur_group[z])):
                temp_map["children"].append(node_map[cur_group[z][n]])
            cur_map["children"].append(temp_map)
    with open(str(y)+".json", "w") as fp:
        json.dump(cur_map, fp)

            
        
    
