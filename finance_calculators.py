import math

#Set boolean values
investment= False
bond= False

#request that user choose which type of calculation they want to do
print("""Chooose either 'Investment' or 'Bond' from the menu below to proceed:

Investment - to calculate the amount of interest you'll earn on an interest
      Bond - to calculate the amount you'll have to pay on a home loan
 
 """)

#store input in variable
calculator= input("Calculator: ").lower()

#if statements that allow user to proceed based on input

#investment calculator
if calculator == "investment":

    #request information from user
    deposit       = float(input("Enter the ammount that are you depositing: "))
    interest_rate = float(input("Enter the inerest rate ('%' Sybmol Not Required): "))
    num_of_years  = float(input("Enter the number of years you plan on investing for: "))
    interest      = input("Do you want 'Simple' or 'Compound' interest: ").lower()

    #simple interest calculation
    if interest == "simple":
        r = interest_rate / 100
        total_with_interest= deposit * (1 + r * num_of_years)
        print(f"R{total_with_interest}")

    #compound interest calculation
    elif interest == "compound":
        r = interest_rate / 100
        total_with_interest = deposit * math.pow((1+r),num_of_years)
        print(f"R{total_with_interest}")

    #incorrect choice entered
    else:
        print("You have entered an inccorect opption!")

#Bond calculator
elif calculator == "bond":
    present_value = float(input("Enter the present value of the house: R"))
    interest_rate = float(input("Enter the inerest rate ('%' Sybmol Not Required): "))
    num_of_months = float(input("Enter the amount of months you plan to take to repay the bond:  "))
    
    #calculations
    monthly_interest  = (interest_rate / 100) / 12
    monthly_repayment = (monthly_interest* present_value)/(1 - (1+monthly_interest)**(-num_of_months))

    #print out monthly repayment
    print(f"R{monthly_repayment}")

#incorret option entered
else:
    print("You have entered an icorrect option.")