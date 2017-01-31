
x = int(input('Enter an Integer'))
if x%2 == 0:
	print('')
	print('Even')
else:
	print('')
	print('Odd')
print('Done')

#Casting - Changing Types
x = int(4)
print(type(x))
x = float(x)
print(type(x))

#Pi
pi = 3.14159
pi_approx = 22/7

#find Area
radius = int(input('Enter Radius: '))
area = pi * (radius**2)

print('')
print('Area: ' + str(area))