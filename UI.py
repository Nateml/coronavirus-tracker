from classes import tracker

valid_options = ['1', '2', '3']
t = tracker.Tracker()

def menu():
    option = input("\n1. Country Search \n2. Tracked Countries \n3. My location \n")

    while(not option in valid_options):
        print("Error - not a valid option")
        option = input("1. Country Search \n2. Tracked Countries \n3. My location \n")
        
    main(option)

def main(option):
    while True:
        if option == valid_options[0]:
            country = input("Country (Type 'back' to go back):\n")
            if country.lower() == "back":
                menu()
            try:
                t.country_search(country)
            except KeyError:
                print("Error - no data available (Make sure you typed in the country name correctly)")
        if option == valid_options[1]:
            menu()
        if option == valid_options[2]:
            menu()

if __name__ == "__main__":
    menu()
    
    