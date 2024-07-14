class Contract:
    def __init__(self, number, name, amount):
        self.number = number
        self.name = name
        self.amount = amount

class ContractBook:
    def __init__(self):
        self.contracts = []

    def add_contract(self, number, name, amount):
        contract = Contract(number, name, amount)
        self.contracts.append(contract)
        print(f"Contract {number} added successfully.")

    def find_contract_by_number(self, number):
        for contract in self.contracts:
            if contract.number == number:
                return contract
        return None

    def find_contract_by_name(self, name):
        found_contracts = []
        for contract in self.contracts:
            if contract.name.lower() == name.lower():
                found_contracts.append(contract)
        return found_contracts

    def display_all_contracts(self):
        if not self.contracts:
            print("No contracts found.")
        else:
            print("List of Contracts:")
            for contract in self.contracts:
                print(f"Number: {contract.number}, Name: {contract.name}, Amount: {contract.amount}")

    def delete_contract(self, number):
        for contract in self.contracts:
            if contract.number == number:
                self.contracts.remove(contract)
                print(f"Contract {number} deleted successfully.")
                return
        print(f"Contract {number} not found.")

# Sample usage of the ContractBook class
if __name__ == "__main__":
    contract_book = ContractBook()

    while True:
        print("\nContract Book Menu:")
        print("1. Add Contract")
        print("2. Find Contract by Number")
        print("3. Find Contracts by Name")
        print("4. Display All Contracts")
        print("5. Delete Contract")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            number = input("Enter contract number: ")
            name = input("Enter contract name: ")
            amount = input("Enter contract amount: ")
            contract_book.add_contract(number, name, amount)

        elif choice == "2":
            number = input("Enter contract number to search: ")
            contract = contract_book.find_contract_by_number(number)
            if contract:
                print(f"Contract found - Number: {contract.number}, Name: {contract.name}, Amount: {contract.amount}")
            else:
                print(f"Contract with number {number} not found.")

        elif choice == "3":
            name = input("Enter contract naclass Contract:
    def __init__(self, number, name, amount):
        self.number = number
        self.name = name
        self.amount = amount

class ContractBook:
    def __init__(self):
        self.contracts = []

    def add_contract(self, number, name, amount):
        contract = Contract(number, name, amount)
        self.contracts.append(contract)
        print(f"Contract {number} added successfully.")

    def find_contract_by_number(self, number):
        for contract in self.contracts:
            if contract.number == number:
                return contract
        return None

    def find_contract_by_name(self, name):
        found_contracts = []
        for contract in self.contracts:
            if contract.name.lower() == name.lower():
                found_contracts.append(contract)
        return found_contracts

    def display_all_contracts(self):class Contract:
    def __init__(self, number, name, amount):
        self.number = number
        self.name = name
        self.amount = amount

class ContractBook:
    def __init__(self):
        self.contracts = []

    def add_contract(self, number, name, amount):
        contract = Contract(number, name, amount)
        self.contracts.append(contract)
        print(f"Contract {number} added successfully.")

    def find_contract_by_number(self, number):
        for contract in self.contracts:
            if contract.number == number:
                return contract
        return None

    def find_contract_by_name(self, name):
        found_contracts = []
        for contract in self.contracts:
            if contract.name.lower() == name.lower():
                found_contracts.append(contract)
        return found_contracts

    def display_all_contracts(self):
        if not self.contracts:
            print("No contracts found.")
        else:
            print("List of Contracts:")
            for contract in self.contracts:
                print(f"Number: {contract.number}, Name: {contract.name}, Amount: {contract.amount}")

    def delete_contract(self, number):
        for contract in self.contracts:
            if contract.number == number:
                self.contracts.remove(contract)
                print(f"Contract {number} deleted successfully.")
                return
        print(f"Contract {number} not found.")

# Sample usage of the ContractBook class
if __name__ == "__main__":
    contract_book = ContractBook()

    while True:
        print("\nContract Book Menu:")
        print("1. Add Contract")
        print("2. Find Contract by Number")
        print("3. Find Contracts by Name")
        print("4. Display All Contracts")
        print("5. Delete Contract")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            number = input("Enter contract number: ")
            name = input("Enter contract name: ")
            amount = input("Enter contract amount: ")
            contract_book.add_contract(number, name, amount)

        elif choice == "2":
            number = input("Enter contract number to search: ")
            contract = contract_book.find_contract_by_number(number)
            if contract:
                print(f"Contract found - Number: {contract.number}, Name: {contract.name}, Amount: {contract.amount}")
            else:
                print(f"Contract with number {number} not found.")

        elif choice == "3":
            name = input("Enter contract naclass Contract:
    def __init__(self, number, name, amount):
        self.number = number
        self.name = name
        if not self.contracts:
            print("No contracts found.")
        else:
            print("List of Contracts:")
            for contract in self.contracts:
                print(f"Number: {contract.number}, Name: {contract.name}, Amount: {contract.amount}")

    def delete_contract(self, number):
        for contract in self.contracts:
            if contract.number == number:
                self.contracts.remove(contract)
                print(f"Contract {number} deleted successfully.")
                return
        print(f"Contract {number} not found.")

# Sample usage of the ContractBook class
if __name__ == "__main__":
    contract_book = ContractBook()

    while True:
        print("\nContract Book Menu:")me to search: ")
            found_contracts = contract_book.find_contract_by_name(name)
            if found_contracts:
                print("Contracts found:")
                for contract in found_contracts:
                    print(f"Number: {contract.number}, Name: {contract.name}, Amount: {contract.amount}")
            else:
                print(f"No contracts found with name '{name}'.")

        elif choice == "4":
            contract_book.display_all_contracts()

        elif choice == "5":
            number = input("Enter contract number to delete: ")
            contract_book.delete_contract(number)

        elif choice == "6":
            print("Exiting Contract Book.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

