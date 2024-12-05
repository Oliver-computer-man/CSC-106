def entername(name):
	print("Enter Name: ")
	return name
	
def add(Quiz, Hw, Exam):
	return Quiz + Hw + Exam

	
print(f"This is your entry: {__name__}")

if __name__ == '__main__':
    print(entername("Someone"))
    print(add(10,20,100))
