import math

print("\n")

n = 1
while n==1:
	num = int(input("Number: "))
	print("Please tell us do you want to find a square root? or do you want to get square of a number?")
	print(f"f = for finding square root of {num}, g = to get square of the number, {num}")
	option = input(str(' '))
	if option == 'f':
		num2 = num
		result = math.trunc(math.sqrt(num2))
		result = "Result: " + str(result) + "\n"
		print(f"square root is = {result}")
	elif option == 'g':
		num3 = num
		out = num3*num3
		print(f"square of the number is = {out}")
		
