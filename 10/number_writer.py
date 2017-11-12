import json

numbers = [2,3.5,7,11, 13]

filename = 'number.json'


def write_from_jsom(file_name, write_date):
	with open(filename, 'w') as f_obj:
		json.dump(write_date, f_obj)


def read_from_json(file_name):
	with open(filename) as f_obj_read:
		numbers_read = json.load(f_obj_read)
	return numbers_read

write_from_jsom(filename, numbers)

print read_from_json(filename)