user_input = ""
low = 0
high = 100
guess = int((high + low)/2)
print("Please think of a number between 0 and 100!")
while user_input != 'c':
	print("Is your secret number",guess,"?")
	user_input = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indiciate the guess is too low. Enter 'c' to indiciate correct guess. "))
	if user_input == 'c':
		print("Game over. Your secret number was:",guess)
		break
	elif user_input == 'h':
		high = guess
	elif user_input == 'l':
		low = guess
	else:
		print("Sorry, I did not understand your input.")
	guess = int((high + low)/2)