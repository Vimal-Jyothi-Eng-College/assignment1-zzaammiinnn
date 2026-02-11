text = input("Enter a string: ")
n = int(input("Enter index to remove: "))
new_text = text[:n] + text[n+1:]

print("New string:", new_text)
