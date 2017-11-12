file_object = open('pi_digits.txt')
content = file_object.read()
print content

with open('pi_digits.txt') as file_object:
	lines = file_object.readlines()
	
for line in lines:
	print line.strip()
	
with open('pi_digits.txt') as file_object:
	content = file_object.read()
print content

new_content = str(content).replace('python', 'fff')
print new_content


message = 'python jj'

print message.replace('python', 'cat')

str = "this is string example....wow!!! this is really string";
print str.replace("is", "was");
print str.replace("is", "was", 3);


with open('new_file.txt','a') as write_file:
	write_file.writelines('asdkjfhaks\n')

