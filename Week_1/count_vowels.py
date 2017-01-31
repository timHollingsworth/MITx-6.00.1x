s = "azcbobobegghakl"
print('Current String: ', s)
count = 0
vowels = "aeiou"
for letter in s:
	if letter in vowels:
		count += 1
print("Number of Vowels: ", str(count))