import json
from typing import List
from record import Record
from persistence import Persistence

class JSONPersistence(Persistence):

    def load_records(self, filepath=None, limit=100) -> List[Record]:
        # If no filepath is specified, the default filepath is loaded
        filename = filepath or Persistence.default_file_path
        print(f"Loading data from: {filename}")
        records = []
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                data = json.load(file)
                for i, row in enumerate(data):
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
        except json.JSONDecodeError:
            print("The file could not be parsed as JSON.")
        return records

    def save_records(self, records: List[Record], filepath) -> None:
        data = []
        for record in records:
            data.append({
                'Date': record.date,
                'Month': record.month,
                'Year': record.year,
                'Company': record.company,
                'Pipeline': record.pipeline,
                'Key Point': record.key_point,
                'Latitude': record.latitude,
                'Longitude': record.longitude,
                'Direction Of Flow': record.direction_of_flow,
                'Trade Type': record.trade_type,
                'Product': record.product,
                'Throughput (1000 m3/d)': record.throughput,
                'Committed Volumes (1000 m3/d)': record.committed_volumes,
                'Uncommitted Volumes (1000 m3/d)': record.uncommitted_volumes,
                'Nameplate Capacity (1000 m3/d)': record.nameplate_capacity,
                'Available Capacity (1000 m3/d)': record.available_capacity,
                'Reason For Variance': record.reason_for_variance
            })
        
        with open(filepath, mode='w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
