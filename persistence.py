from abc import ABC, abstractmethod
from typing import List
from record import Record

class Persistence(ABC):
    default_file_path = r"C:\Users\Aaron2\Desktop\Semester4\Language Research Project\keystone-throughput-and-capacity-fixed.csv"
    @abstractmethod
    def load_records(self, filepath=None, limit=100) -> List[Record]:
        """Load records from a data source."""
        pass

    @abstractmethod
    def save_records(self, records: List[Record], filepath) -> None:
        """Save records to a data source."""
        pass
