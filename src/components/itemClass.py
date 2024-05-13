class Entry():
    def __init__(self, job = "-", date="-", description = "-", amount = 0.0):
        self.job = job
        self.date = date
        self.description = description
        self.amount = amount
    
    def to_dict(self):
        return {
            'job': self.job,
            'date': self.date,
            'description': self.description,
            'amount': self.amount
        }

    def __str__(self):
        return f"{self.job} - {self.date} - {self.description} - {self.amount}"
    
    def print(self):
        print(f"{self.job} - {self.date} - {self.description} - {self.amount}")