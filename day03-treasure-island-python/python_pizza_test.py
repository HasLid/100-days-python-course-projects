print("welcome to python pizza delivery")
bill = 0
size = input("what size pizza do you want? S, M or L:")
if size == "S":
    bill = 15
    print("pizza: $15")
elif size == "M":
    bill = 20
    print("pizza: $20")
elif size == "L":
    bill = 25
    print("pizza: $25")
    

peperoni = input("do you want peperoni? type Y for yes or N for no:")
if peperoni == "Y":
    size == "S"
    bill += 2
print("peperoni added: +$2")

extra_cheese = input("do you want extra cheese? type Y for yes or N for no ")
if extra_cheese == "Y":
    bill =+ 1
    print("extra cheese addea: +$1")

print(f"Final bill: ${bill}")