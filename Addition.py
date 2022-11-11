########################################################
# Demonstration of Addition using import AdditionModule
########################################################

import AdditionModule

def main():
	print("Enter first number : ")
	No1 = int(input())

	print("Enter second number : ")
	No2 = int(input())

	Addition = AdditionModule.Addition(No1,No2)
	print("Addition is : ",Addition)

if __name__=="__main__":
	main()


########################################################
#	Input	:	Enter first number :
#				10
#				Enter second number :
#				20
#	Output	:	Addition is :  30
########################################################