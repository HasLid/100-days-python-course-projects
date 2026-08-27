age = int(input("Your age: "))
status = input("Mr, Miss or Mrs: ").upper()
name = input("Your name: ")
if age >= 18:
    print(f"Hello, {status} {name}, This show is not for Adults!.")
else:
    print(f"Hello, {status}{ name}, You are welcome!.")