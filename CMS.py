import random

customers = []

print("Welcome to my Customer Management System. You can add, search, delete, and modify customers.")

def get_id():
    existing_ids = {customer[0] for customer in customers}
    while True:
        customer_id = random.randint(1000000, 9999999)
        if customer_id not in existing_ids:
            return customer_id

def get_phone(): # A get method to check whether the phone number is of 10 digits as well as in numeric values
    while True:
        try:
            number = input("Phone Number: ")
            if number.isdigit() and len(number) == 10:
                return int(number)
            else:
                print("Please enter a valid 10-digit phone number.")
        except ValueError:
            print("Invalid input. Please enter a numeric phone number.")

def add_customer():
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    gender = input("Gender: ")
    age = input("Age: ")
    phone = get_phone()
    email = input("Email: ")
    country = input("Country: ")
    city = input("City: ")
    pincode = input("Pincode: ")
    occupation = input("Occupation: ")

    customer = [
        get_id(),
        firstName,
        lastName,
        gender,
        age,
        phone,
        email,
        country,
        city,
        pincode,
        occupation
    ]
    customers.append(customer)
    print(f"{firstName} {lastName} added successfully.")

def search_customer():
    phone = get_phone()
    for customer in customers:
        if phone == customer[5]:
            print("Customer Found:", customer)
            return
    print("Customer Not Found. Try again.")

def delete_customer():
    phone = get_phone()
    for customer in customers:
        if phone == customer[5]:
            customers.remove(customer)
            print(f"Customer removed successfully: {customer}")
            return
    print("Customer Not Found. Try again.")

def modify_customer():
    phone = get_phone()
    for customer in customers:
        if phone == customer[5]:
            print("Enter the details of the customer to be modified (leave blank if you don't want to change): ")
            firstName = input("First Name: ") or customer[1]
            lastName = input("Last Name: ") or customer[2]
            gender = input("Gender: ") or customer[3]
            age = input("Age: ") or customer[4]
            new_phone = input("Phone: ") or customer[5]
            if new_phone:
                new_phone = int(new_phone)
            email = input("Email: ") or customer[6]
            country = input("Country: ") or customer[7]
            city = input("City: ") or customer[8]
            pincode = input("Pincode: ") or customer[9]
            occupation = input("Occupation: ") or customer[10]

            customer[1] = firstName
            customer[2] = lastName
            customer[3] = gender
            customer[4] = age
            customer[5] = new_phone
            customer[6] = email
            customer[7] = country
            customer[8] = city
            customer[9] = pincode
            customer[10] = occupation

            print("Customer Modified Successfully:", customer)
            return
    print("Customer Not Found. Try again.")

def display_all_customers():
    if not customers:
        print("No customers found.")
    else:
        for customer in customers:
            print(customer)

def main():
    actions = {
        '1': add_customer,
        '2': search_customer,
        '3': delete_customer,
        '4': modify_customer,
        '5': display_all_customers,
        '6': exit
    }

    while True:
        print("\nCustomer Management System")
        print("1. Add Customer")
        print("2. Search Customer")
        print("3. Delete Customer")
        print("4. Modify Customer")
        print("5. Display All Customers")
        print("6. Exit")
        choice = input("Enter your choice: ")

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
