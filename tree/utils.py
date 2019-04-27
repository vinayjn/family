import json

from .models import Member


def get_json(root, members, node_id, depth):
	data = {}	
	data["children"] = []
	data["nodeName"] = root.name
	data["name"] = root.name	
	data["code"] = "N" + node_id
	data["type"] = "type" + str(depth)
	data["label"] = root.name
	data["version"] = "v1.0"
	data["link"] = {
		"name" : "Link NODE NAME 1",
		"nodeName" : root.name,
		"direction" : "ASYN"
	}
	children = sorted(list(filter(lambda x: x.parent == root, members)), key=lambda x: x.id)
	for index, child in enumerate(children):
		node_id = str(depth + 1) + "." + str(index + 1)
		data["children"].append(get_json(child, members, node_id, depth + 1))
	return data

def get_json_tree():
	members = Member.objects.all()
	root = members[0]
	json_data = get_json(root, members, "1", 1)	
	return json.dumps({"tree": json_data})
