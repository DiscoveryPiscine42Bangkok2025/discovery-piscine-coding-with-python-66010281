number_str = input("Give me a number: ")
number = float(number_str)
if number == int(number):
    print(int(number))
elif number > 0:
    print(int(number) + 1)
else:
    print(int(number)) 
