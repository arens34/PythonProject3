from business import Business
from record import Record
import re

class Presentation:
    """
    Handles the user interface and interaction for managing records.
    
    This class provides methods for displaying menus, loading and saving data,
    displaying all records or a single record, adding, editing, and deleting records.
    """

    def __init__(self):
        """
        Initializes the Presentation layer, loading the Business layer and setting
        the persistence subclass.
        """
        self.business = Business()

    def display_menu(self):
        """
        Displays the main menu options to the user and prompts for their choice.
        """
        if self.business.data_loaded:
            print("Full Name: Aaron Renshaw\n")
            print("1. Load Data")
            print("2. Save Data")
            print("3. Display All Records")
            print("4. Display Single Record")
            print("5. Add Record")
            print("6. Edit Record")
            print("7. Delete Record")
            print("8. Exit")
            choice = input("Select an option: ")
            self.handle_choice(choice)
        else:
            self.load_data()

    def handle_choice(self, choice):
        """
        Handles the user's menu choice and directs the program flow accordingly.

        Parameters:
            choice (str): The user's selected option from the menu.
        """
        if choice == '1':
            self.load_data()
        elif choice == '2':
            self.save_data()
        elif choice == '3':
            self.display_records()
        elif choice == '4':
            self.display_single_record()
        elif choice == '5':
            self.add_record()
        elif choice == '6':
            self.edit_record()
        elif choice == '7':
            self.delete_record()
        elif choice == '8':
            exit()
        else:
            print("Invalid option. Please try again.")

    def load_data(self):
        """
        Loads data from the default file path into the business layer.
        """
        filename = input("Enter the filename to load records from, or press enter to load the default: ")
        if self.validate_filename(filename):
            self.business.load_data(filename)

    def save_data(self):
        """
        Prompts the user for a filename and saves the current records to that file.
        """
        filename = input("Enter the filename to save records, or press enter to save to currently loaded file: ")
        if self.validate_filename(filename):
            self.business.save_data(filename)

    def display_records(self):
        """
        Displays all records currently loaded in the business layer.
        """
        records = self.business.get_all_records()
        if records:
            for record in records:
                print(f"Date: {record.date}")
                print(f"Month: {record.month}")
                print(f"Year: {record.year}")
                print(f"Company: {record.company}")
                print(f"Pipeline: {record.pipeline}")
                print(f"Key Point: {record.key_point}")
                print(f"Latitude: {record.latitude}")
                print(f"Longitude: {record.longitude}")
                print(f"Direction Of Flow: {record.direction_of_flow}")
                print(f"Trade Type: {record.trade_type}")
                print(f"Product: {record.product}")
                print(f"Throughput (1000 m3/d): {record.throughput}")
                print(f"Committed Volumes (1000 m3/d): {record.committed_volumes}")
                print(f"Uncommitted Volumes (1000 m3/d): {record.uncommitted_volumes}")
                print(f"Nameplate Capacity (1000 m3/d): {record.nameplate_capacity}")
                print(f"Available Capacity (1000 m3/d): {record.available_capacity}")
                print(f"Reason For Variance: {record.reason_for_variance}")
                print(f"{self.business.record_count} records displayed.")
                print()
        else:
            print("No records found.")

    def display_single_record(self):
        """
        Displays a single record based on the index provided by the user.

        Prompts the user for an index, retrieves the corresponding record from
        the business layer, and prints its details.
        """


        print(f"\nThere are {self.business.record_count} records.")
        index = int(input("Enter the index of the record to display: "))
        record = self.business.get_record(index)

        if record:
            print(f"Date: {record.date}")
            print(f"Month: {record.month}")
            print(f"Year: {record.year}")
            print(f"Company: {record.company}")
            print(f"Pipeline: {record.pipeline}")
            print(f"Key Point: {record.key_point}")
            print(f"Latitude: {record.latitude}")
            print(f"Longitude: {record.longitude}")
            print(f"Direction Of Flow: {record.direction_of_flow}")
            print(f"Trade Type: {record.trade_type}")
            print(f"Product: {record.product}")
            print(f"Throughput (1000 m3/d): {record.throughput}")
            print(f"Committed Volumes (1000 m3/d): {record.committed_volumes}")
            print(f"Uncommitted Volumes (1000 m3/d): {record.uncommitted_volumes}")
            print(f"Nameplate Capacity (1000 m3/d): {record.nameplate_capacity}")
            print(f"Available Capacity (1000 m3/d): {record.available_capacity}")
            print(f"Reason For Variance: {record.reason_for_variance}")
        else:
            print("\nNo record found at the specified index.")

    def add_record(self):
        """
        Prompts the user for record data and adds it to the business layer.
        """
        record_data = self.get_record_input()
        record = Record(**record_data)
        self.business.add_record(record)

    def edit_record(self):
        """
        Prompts the user for an index of a record to edit and updates it with new data.

        The user provides the index and the new data for the record.
        """
        index = int(input("Enter the index of the record to edit: "))
        record_data = self.get_record_input()
        record = Record(**record_data)
        self.business.edit_record(index, record)

    def delete_record(self):
        """
        Prompts the user for an index of a record to delete and removes it from the business layer.
        """
        index = int(input("Enter the index of the record to delete: "))
        self.business.delete_record(index)

    def get_record_input(self):
        """
        Collects input from the user to create a new record.

        Returns:
            dict: A dictionary containing the record's attributes and their values.
        """
        return {
            'date': input("Enter Date: "),
            'month': input("Enter Month: "),
            'year': input("Enter Year: "),
            'company': input("Enter Company: "),
            'pipeline': input("Enter Pipeline: "),
            'key_point': input("Enter Key Point: "),
            'latitude': input("Enter Latitude: "),
            'longitude': input("Enter Longitude: "),
            'direction_of_flow': input("Enter Direction Of Flow: "),
            'trade_type': input("Enter Trade Type: "),
            'product': input("Enter Product: "),
            'throughput': input("Enter Throughput (1000 m3/d): "),
            'committed_volumes': input("Enter Committed Volumes (1000 m3/d): "),
            'uncommitted_volumes': input("Enter Uncommitted Volumes (1000 m3/d): "),
            'nameplate_capacity': input("Enter Nameplate Capacity (1000 m3/d): "),
            'available_capacity': input("Enter Available Capacity (1000 m3/d): "),
            'reason_for_variance': input("Enter Reason For Variance: ")
        }

    def validate_filename(self, filename):
        # Return true if no filename is entered (user chose default)
        if not filename:
            return True
        if re.search(r'\.csv$', filename, re.IGNORECASE) or re.search(r'\.json$', filename, re.IGNORECASE):
            return True
        else:
            print(f"\nError: File must end with .csv or .json\n")
            return False