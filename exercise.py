print("welcome to the rollercoaster")
height = int(input("what is your height in cm? "))
bill = 0

if height >= 120:
    print("you can ride the roller coaster")
    age = int(input("what is your age? "))
    
    if age < 12:
        bill = 5
        print("child ticket are $5.")
    elif age <= 18:
        bill = 7
        print("youth ticket are $7.")
    else:
        bill = 12
        print("adult ticket are $12.")
    
    want_photo = input("Do you want a photo? type y for yes or n for No. ").lower()
    if want_photo == "y":
        bill += 3
    
    print(f"Your final bill is: ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")