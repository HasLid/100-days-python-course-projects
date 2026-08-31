print ("Welcome to the tip calculator!")
bill = float(input("How much is bill? $"))
tip = int(input("How much tip would like to give? "))
people = int(input("How many people to pay the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
each_person = total_bill / people
final_amount = round(each_person)
print (f"Each person should pay: ${final_amount}")