print("welcome to python pizza delivery")
bill = 0
size = input("what size pizza do you want? s, m or l:")
if size == "s":
    bill = 15
    print("pizza: $15")
if size == "m":
    bill = 20
    print("pizza: $20")
if size == "l":
    bill = 25
    print("pizza: $25")
    print(f"bill: ${bill}")

add = input("add peperoni for small pizza? type y for yes or n for no:")
if add == "y":
    bill += 2
    print("for small pizza: $2")
    print(f"bill: ${bill}")   

add = input("add peperoni for medium or large pizza: y or n:")
if add == "y":
    bill += 3
    print("for medium or large pizza: $3")
    print(f"bill: ${bill}")

add = input("add extra cheese for any size of pizza: y or n:")
if add == "y":
    bill += 1
    print("add extra cheese for any size of pizza: $1")
else:
    print("you have not sellect anything.")

print(f"final bill: ${bill}")

