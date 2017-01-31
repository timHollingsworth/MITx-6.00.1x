s = "azcbobobegghakl"
count = 0
location = -1
while True:
	location = s.find('bob', location + 1)
	if location == -1: break
	count += 1
print('Number of times bob occurs is: ', str(count))