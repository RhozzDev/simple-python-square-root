import math

print "\n"

num = input("Number: ")

def sroot(base):
	result = math.trunc(math.sqrt(base))
	result = "Result: " + str(result) + "\n"
	return result
	
print sroot(num)
