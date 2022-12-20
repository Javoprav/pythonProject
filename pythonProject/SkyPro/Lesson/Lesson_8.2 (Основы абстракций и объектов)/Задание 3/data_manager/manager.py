import json

def load_data():
	with open("data_manager/data.json") as file:
		data = json.load(file)
	return data