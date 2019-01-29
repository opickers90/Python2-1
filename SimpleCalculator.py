while True:
	print("Options.")
	print("Enter 'add' to add two numbers")
	print("Enter 'subtract' to subtract two numbers")
	print("Enter 'multiply' to multiply two numbers")
	print("Enter 'divide' to divide two numbers")
	print("Enter 'power of' to divide two numbers")
	print("Enter 'square root' to divide two numbers")
	print("Enter 'floor division' to divide two numbers")
	print("Enter 'modulos' to divide two numbers")
	print("Enter 'quit' to end the program")
	user_input = input(": ")

	if user_input == "quit":
		break
	elif user_input == "add":
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
		result = str(num1 + num2)
		print ("The answer is: " + result)
		print()
	elif user_input == "subtract":
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
		result = str(num1 - num2)
		print ("The answer is: " + result)
		print()
	elif user_input == "multiply":
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
		result = str(num1 * num2)
		print ("The answer is: " + result)
		print()
	elif user_input == "divide":
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
		while num2 == 0:
			num2 = float(input("Second Number cannot 0, Enter second Number: "))
			if num2 != 0 :
				break
		result = str(num1 / num2)
		print ("The answer is: " + result)
		print()
	elif user_input == "power of":
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
		result = str(num1 ** num2)
		print ("The answer is: " + result)
		print()
	elif user_input == "square root":
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
		result = str(num1 ** (1/ num2))
		print ("The answer is: " + result)
		print()
	elif user_input == "floor division":
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
		result = str(num1 // num2)
		print ("The answer is: " + result)
		print()
	elif user_input == "modulos":
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
		result = str(num1 % num2)
		print ("The answer is: " + result)
		print()
	else:
		print("Unknown input")

