import sys
from MyClass import MyClass

def main():
	lst = []
	while (True):
		try :
			x = input('Enter class name : ')
			lst = x.split(" ")
		except KeyboardInterrupt:
			exit()
		for i in lst :
			if (i == "exit"):
				exit()
			test = MyClass(i)
			test.create_cpp()
			test.create_hpp()

if __name__ == "__main__":
	main()