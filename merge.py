import json

with open('file1 1.json', 'r') as file1:
	file1_dict = json.load(file1)
	
with open('file2 1.json', 'r') as file2:
	file2_dict = json.load(file2)
	
path_revisions_dict = {}
	
for path_revision_obj in file2_dict:
	key = path_revision_obj['path']
	value = path_revision_obj['revisions']
	path_revisions_dict[key] = value
	
output_json_array = []
	
for component in file1_dict['components']:
	if component['path'] in path_revisions_dict.keys():	
		output_json_array_element = {}
		output_json_array_element['path'] = component['path']
		output_json_array_element['revisions'] = path_revisions_dict[component['path']]
		output_json_array_element[component['measures']['metric']] = component['measures']['value']
		output_json_array.append(output_json_array_element)
		
with open('file3.json', 'w') as json_file3:
  json.dump(output_json_array, json_file3)
