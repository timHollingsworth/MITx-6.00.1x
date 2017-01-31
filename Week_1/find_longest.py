s = "hlzykgphknfeqty"
longest = ""
current = ""
for letter in s:
	if letter > current[-1:] or current[-1:] == letter:
		current += letter
	else:
		if len(current) > len(longest):
			longest = current
		current = letter
if len(current) > len(longest):
	longest = current
if len(longest) <= 0:
	longest = s
print('Longest substring in alphabetical order is: ', longest)