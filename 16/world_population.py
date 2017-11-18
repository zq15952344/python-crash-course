import json

from country_code import get_country_code

filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)

print pop_data

cc_populations = []

for pop_dic in pop_data:
	
	if pop_dic['Year'] == '2010':
		country_name = pop_dic['Country Name']
		poulation = int(float(pop_dic['Value']))
		
		code = get_country_code(country_name)
		if code:
			print code + " " + str(poulation)
		else:
			code = country_name
		cc_population = {}
		cc_population[code]=str(poulation)
		cc_populations.append(cc_population)
