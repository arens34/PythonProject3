class Record:
    """
    Represents a record from the dataset.

    Attributes:
        date (str): The date of the record.
        month (str): The month of the record.
        year (str): The year of the record.
        company (str): The name of the company.
        pipeline (str): The name of the pipeline.
        key_point (str): A key point related to the record.
        latitude (float): The latitude associated with the record.
        longitude (float): The longitude associated with the record.
        direction_of_flow (str): The direction of flow.
        trade_type (str): The type of trade.
        product (str): The product associated with the record.
        throughput (float): The throughput in 1000 m3/d.
        committed_volumes (float): The committed volumes in 1000 m3/d.
        uncommitted_volumes (float): The uncommitted volumes in 1000 m3/d.
        nameplate_capacity (float): The nameplate capacity in 1000 m3/d.
        available_capacity (float): The available capacity in 1000 m3/d.
        reason_for_variance (str): The reason for variance.
    """

    def __init__(self, date, month, year, company, pipeline, key_point, latitude, longitude,
                 direction_of_flow, trade_type, product, throughput, committed_volumes,
                 uncommitted_volumes, nameplate_capacity, available_capacity, reason_for_variance):
        """
        Initializes a Record instance.

        Args:
            date (str): The date of the record.
            month (str): The month of the record.
            year (str): The year of the record.
            company (str): The name of the company.
            pipeline (str): The name of the pipeline.
            key_point (str): A key point related to the record.
            latitude (float): The latitude associated with the record.
            longitude (float): The longitude associated with the record.
            direction_of_flow (str): The direction of flow.
            trade_type (str): The type of trade.
            product (str): The product associated with the record.
            throughput (float): The throughput in 1000 m3/d.
            committed_volumes (float): The committed volumes in 1000 m3/d.
            uncommitted_volumes (float): The uncommitted volumes in 1000 m3/d.
            nameplate_capacity (float): The nameplate capacity in 1000 m3/d.
            available_capacity (float): The available capacity in 1000 m3/d.
            reason_for_variance (str): The reason for variance.
        """
        self.date = date
        self.month = month
        self.year = year
        self.company = company
        self.pipeline = pipeline
        self.key_point = key_point
        self.latitude = latitude
        self.longitude = longitude
        self.direction_of_flow = direction_of_flow
        self.trade_type = trade_type
        self.product = product
        self.throughput = throughput
        self.committed_volumes = committed_volumes
        self.uncommitted_volumes = uncommitted_volumes
        self.nameplate_capacity = nameplate_capacity
        self.available_capacity = available_capacity
        self.reason_for_variance = reason_for_variance

    def __str__(self):
        """
        Returns a string representation of the Record instance.

        Returns:
            str: A formatted string containing all attributes of the record.
        """
        return (f"Date: {self.date}, Month: {self.month}, Year: {self.year}, Company: {self.company}, "
                f"Pipeline: {self.pipeline}, Key Point: {self.key_point}, Latitude: {self.latitude}, "
                f"Longitude: {self.longitude}, Direction: {self.direction_of_flow}, "
                f"Trade Type: {self.trade_type}, Product: {self.product}, "
                f"Throughput: {self.throughput}, Committed Volumes: {self.committed_volumes}, "
                f"Uncommitted Volumes: {self.uncommitted_volumes}, Nameplate Capacity: {self.nameplate_capacity}, "
                f"Available Capacity: {self.available_capacity}, Reason For Variance: {self.reason_for_variance}")
