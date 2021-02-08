print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

Small=15
Medium=20
Large=25

if size=="S":
    print("Small pizza cost is 15")
    if add_pepperoni=="Y":
        Small+=2
        print(f"cost is  {Small} with pepperoni")
        if extra_cheese=="Y":
            Small+=1
            print(f"cost is  {Small} with extra cheese")
        else:
            print(f"cost is {Small}")    
    else:
        print(f"cost is {Small}")    
elif size=="M":
    print("Medium pizza cost is 20")
    if add_pepperoni=="Y":
        Medium+=3
        print(f"cost is {Medium } with pepperoni")
        if extra_cheese=="Y":
            Medium+=1
            print(f"cost is  {Medium} with extra cheese")
        else:
            print(f"cost is {Medium}")    
    else:
        print(f"cost is {Medium}")   
else:
    print("Large pizza cost is 25")
    if add_pepperoni=="Y":
        Large+=3
        print(f"cost is {Large} with pepperoni")
        if extra_cheese=="Y":
            Large+=1
            print(f"cost is  {Large} with extra cheese")
        else:
            print(f"cost is {Large}") 
    else:
        print(f"cost is {Large}")
              
