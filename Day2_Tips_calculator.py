print("Welcome to the tip calculator!!!")
rupee_symbol = u"\u20B9"

bill   =  float(input("What was the total bill? {}".format(rupee_symbol) ))
tip    =  int(input("How much tip would you like to give? 10,12 or 15? "))
people =  int(input("How many people to split the bill? "))

bill_tip = bill * tip /100 + bill 
total_amount_distribute = bill_tip / people

print("Each person should pay: {0}{1}" .format(rupee_symbol,total_amount_distribute))
