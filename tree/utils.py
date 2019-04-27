import json

from .models import Member


def get_json(root, members):
	data = {}
	data["nodeName"] = root.name
	data["children"] = []
	children = sorted(list(filter(lambda x: x.parent == root, members)), key=lambda x: x.order)
	for child in children:
		data["children"].append(get_json(child, members))
	return data

def get_json_tree():
	members = Member.objects.all()
	root = members[0]
	json_data = get_json(root, members)
	return json.dumps(json_data)
