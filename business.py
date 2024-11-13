from json_persistence import JSONPersistence
from csv_persistence import CSVPersistence
from persistence import Persistence
import re

class Business:
    def __init__(self):
        """Initialize the Business object with a persistence strategy and an empty list of records.

        Args:
            persistence (Persistence): An instance of a class that implements the Persistence interface.
        """
        self.records = []
        self.persistence = None
        #Stores the count of records
        self.record_count = 0
        self.data_loaded = False
        self.loaded_filename = ""

    def load_data(self, filename):
        """Load records from a specified file using the persistence strategy.

        Args:
            filename (str): The path to the file to load records from.

        Returns:
            None
        """

        # If filename is empty, choose default file path
        if not filename:
            filename = Persistence.default_file_path

        self.choose_persistence_strategy(filename)

        self.records = self.persistence.load_records(filename)
        self.data_loaded = True
        self.loaded_filename = filename
        self.update_record_count()

    def save_data(self, filename):
        """Save the current records to a specified file using the persistence strategy.

        Args:
            filename (str): The path to the file where records will be saved.

        Returns:
            None
        """
        # If filename is empty, save to the file that is currently loaded
        if not filename:
            filename = self.loaded_filename

        self.choose_persistence_strategy(filename)

        self.persistence.save_records(self.records, filename)

    def get_record(self, index):
        """Retrieve a specific record by its index.

        Args:
            index (int): The index of the record to retrieve.

        Returns:
            Record: The Record object at the specified index, or None if the index is out of bounds.
        """
        adjusted_index = index - 1
        return self.records[adjusted_index] if adjusted_index < len(self.records) and adjusted_index >= 0 else None

    def get_all_records(self):
        """Get a list of all records.

        Returns:
            list: A list of all Record objects stored in the business.
        """
        return self.records

    def add_record(self, record):
        """Add a new record to the business's records.

        Args:
            record (Record): The Record object to add.

        Returns:
            None
        """
        self.records.append(record)
        self.update_record_count()

    def edit_record(self, index, updated_record):
        """Edit an existing record at the specified index.

        Args:
            index (int): The index of the record to edit.
            updated_record (Record): The updated Record object to replace the existing one.

        Returns:
            None
        """
        if index < len(self.records):
            self.records[index] = updated_record

    def delete_record(self, index):
        """Delete a record at the specified index.

        Args:
            index (int): The index of the record to delete.

        Returns:
            None
        """
        adjusted_index = index - 1
        if adjusted_index < len(self.records):
            del self.records[adjusted_index]
            self.update_record_count()

    # Updates record count after any method that loads, adds, removes records
    def update_record_count(self):
        self.record_count = len(self.records)

    # Logic to choose the persistence subclass based on the filename
    def choose_persistence_strategy(self, filename):
        if re.search(r'\.csv$', filename, re.IGNORECASE):
            self.persistence = CSVPersistence()
        elif re.search(r'\.json$', filename, re.IGNORECASE):
            self.persistence = JSONPersistence()
        else:
            raise ValueError("Unsupported file format")