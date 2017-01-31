"""
Type Errors:
    SyntaxError: Python can't parse program
    NameError: local or global name not found
    AttributeError: attribute reference fails
    TypeError: operand doesn't have correct TypeError
    ValueError: operand type okay, but value is illegal
    IOError: IO system reports mfalfunction (File not found)

What to Do:
    stop execution, signal error condition
    in python: raise an exception
    raise Exception("descriptive string")

else:
    body of this is executed when excution of associated try body completes with no exceptions

finally:
    body of this is always executed after try, else and exceptions
    clauses if they raised another error or executed a break,
    continue
"""

# try:
#     a = int(input("Tell me one number"))
#     b = int(input("Tell me another number"))
#     print(a/b)
#     print ("Okay")
# except ValueError:
#     print("Could not convert to number")
# except ZeroDivisionError:
#     print("Could not divide by zero")
# except:
#     print("Bug in user input")
# print("Outside")

# while True:
#     try:
#         n = input("Please enter an integer")
#         n = int(n)
#         break
#     except ValueError:
#         print("Input not an integer; try again")
# print("Correct input of an integer")

# data = []
#
# file_name = input("Provide a name of a file of data ")
#
# try:
#     fh = open(file_name, "r")
# except IOError:
#     print('cannot open ',file_name)
# else:
#     for new in fh:
#         if new != '\n':
#             addIt = new[:-1].split(',')
#             data.append(addIt)
# finally:
#     fh.close()

# raise ValueError("something is wrong")

# def get_ratios(L1, L2):
#     ratios = []
#
#     for index in range(len(L1)):
#         try:
#             ratios.append(L1[index]/float(L2[index]))
#         except ZeroDivisionError:
#             ratios.append(float('NaN')) #NaN not a member
#         except:
#             raise ValueError('get_ratios called with bad arg')
#     return ratios
#
# def get_stats(class_list):
#     new_stats = []
#     for elt in class_list:
#         new_stats.append([elt[0], elt[1], avg(elt[1])])
#     return new_stats
#
# def avg(grades):
#     try:
#         return round(sum(grades)/len(grades),2)
#     except ZeroDivisionError:
#         print("No Grade Data")
#         return 0.0
#
# test_grades = [[['bruce', 'wayne'],[88, 75, 96]], [['peter', 'parker'],[67,86,95]],[['deadpool'],[]]]
#
# print(test_grades)
# print("Average grades",get_stats(test_grades))
