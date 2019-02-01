from ViewPresenter import ViewPresenter

license_plate = None
brand = None
model = None
year = None
color = None
choice = None


def display_menu():
    print(">>>>Program Start>>>>")

    print(">>Menu \n    1) Press \"1\" for add a vehicle \n    2) Press \"2\" for removed a vehicle \n"
          "    3) Press \"3\" for print board content \n    4) Press \"4\" for quit the application \n"
          "    5) Press \"?\" for print that menu")


display_menu()

while choice != '4':
    choice = input(">>Choose option:\n")
    if choice == '1':
        print(">>Pressed option is ", choice)
        license_plate = input(">>License plate:\n")
        if license_plate is None:
            print("Error: license plate is not correct, you must enter valid license plate")
        else:
            brand = input(">>Brand:\n")
            model = input(">>Model:\n")
            year = input(">>Year:\n")
            color = input(">>Color:\n")

            message = ViewPresenter.add_vehicle(brand, model, license_plate, year)
            print(message)
            print(ViewPresenter.get_availabilities())

    elif choice == '2':
        print(">>Pressed option is ", choice)
        license_plate = input("Enter a license plate:\n")
        message = ViewPresenter.remove_vehicle(license_plate)
        print(message)
        print(ViewPresenter.get_availabilities())

    elif choice == '3':
        print(">>Pressed option is ", choice)
        print(ViewPresenter.get_availabilities())
    elif choice == '4':
        print(">>Pressed option is ", choice)
    elif choice == "?":
        print(">>Pressed option is ", choice)
        display_menu()

print(">>>>Program End>>>>")
