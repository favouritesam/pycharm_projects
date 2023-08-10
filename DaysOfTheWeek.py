user_choice: bool = True
while user_choice:
    numbers = int(input("Enter number between range 1-7:"))
    if numbers == 1:
        print("monday")
    if numbers == 2:
        print("tuesday")
    if numbers == 3:
        print("wednesday")
    if numbers == 4:
        print("thursday")
    if numbers == 5:
        print("friday")
    if numbers == 6:
        print("saturday")
    if numbers == 7:
        print("sunday")
    if numbers < 1 or numbers > 7:
        print("knw your limit")
    user_choice = bool((input("Enter True to continue or False to Quit: ")).title())
    quit()



