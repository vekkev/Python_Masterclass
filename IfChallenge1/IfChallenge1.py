
name = input("Please enter your First Name: ")
age = int(input("PLease tell me your age: "))

if 18 <= age < 31:
	print("Welcome to Holiday")
elif age < 18:
	print("Please come back in {} year(´s)".format(18-age))
elif age > 30:
	print("Sorry, but you´re too old! Maybe you find another holiday for adult people.")

