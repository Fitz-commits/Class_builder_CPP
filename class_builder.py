import sys
from MyClass import MyClass

def main():
	lst = []
	while (True):
		try :
			x = input('Enter class name : ')
			lst = x.split(" ")
			print(lst)
		except KeyboardInterrupt:
			exit()
			for i in lst :
				try :
					float(i)
					print("is a number")
					continue
				except ValueError:
					if (i == "exit"):
						exit()
					test = MyClass(i)
					test.create_cpp()
					test.create_hpp()

if __name__ == "__main__":
	main()