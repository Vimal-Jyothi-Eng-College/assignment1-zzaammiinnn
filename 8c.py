my_dict = {"name": "Zamin", "age": 20, "course": "CS"}

key = input("Enter key to check: ")

if key in my_dict:
    print("Key exists")
else:
    print("Key does not exist")
