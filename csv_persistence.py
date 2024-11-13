import csv
from typing import List
from record import Record
from persistence import Persistence

class CSVPersistence(Persistence):

    def load_records(self, filepath=None, limit=100) -> List[Record]:
        # If no filepath is specified, the default filepath is loaded
        filename = filepath or Persistence.default_file_path
        print(f"Loading data from: {filename}")
        records = []
        try:
            with open(filename, mode='r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                for i, row in enumerate(reader):
                    if i >= limit:
                        break
                    record = Record(
                        date=row['Date'].strip(),
                        month=row['Month'].strip(),
                        year=row['Year'].strip(),
                        company=row['Company'].strip(),
                        pipeline=row['Pipeline'].strip(),
                        key_point=row['Key Point'].strip(),
                        latitude=row['Latitude'].strip(),
                        longitude=row['Longitude'].strip(),
                        direction_of_flow=row['Direction Of Flow'].strip(),
                        trade_type=row['Trade Type'].strip(),
                        product=row['Product'].strip(),
                        throughput=row['Throughput (1000 m3/d)'].strip(),
                        committed_volumes=row['Committed Volumes (1000 m3/d)'].strip(),
                        uncommitted_volumes=row['Uncommitted Volumes (1000 m3/d)'].strip(),
                        nameplate_capacity=row['Nameplate Capacity (1000 m3/d)'].strip(),
                        available_capacity=row['Available Capacity (1000 m3/d)'].strip(),
                        reason_for_variance=row['Reason For Variance'].strip()
                    )
                    records.append(record)
        except FileNotFoundError:
            print("The specified file was not found.")
        return records

    def save_records(self, records: List[Record], filepath) -> None:

        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Month', 'Year', 'Company', 'Pipeline', 'Key Point', 'Latitude',
                             'Longitude', 'Direction Of Flow', 'Trade Type', 'Product',
                             'Throughput (1000 m3/d)', 'Committed Volumes (1000 m3/d)', 
                             'Uncommitted Volumes (1000 m3/d)', 'Nameplate Capacity (1000 m3/d)', 
                             'Available Capacity (1000 m3/d)', 'Reason For Variance'])
            for record in records:
                writer.writerow([
                    record.date, record.month, record.year, record.company, record.pipeline, 
                    record.key_point, record.latitude, record.longitude, record.direction_of_flow, 
                    record.trade_type, record.product, record.throughput, 
                    record.committed_volumes, record.uncommitted_volumes, 
                    record.nameplate_capacity, record.available_capacity, 
                    record.reason_for_variance
                ])
