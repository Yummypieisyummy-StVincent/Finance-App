class Entry():
    def __init__(self, job="-", date="-", description="-", amount=0.0, category="-", client_name="-", taxable=False, payment_status="Pending", savings_percentage=0):
        self.job = job
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category
        self.client_name = client_name
        self.taxable = taxable
        self.payment_status = payment_status  # "Paid", "Pending", "Overdue"
        self.savings_percentage = savings_percentage
    
    @property
    def savings_amount(self):
        """Compute savings based on percentage"""
        if self.savings_percentage is None:
            return 0.0
        return round(self.amount * (self.savings_percentage / 100), 2)
    
    def to_dict(self):
        data = {
            'job': self.job,
            'date': self.date,
            'description': self.description,
            'amount': self.amount,
            'category': self.category,
            'client_name': self.client_name,
            'taxable': self.taxable,
            'payment_status': self.payment_status
        }
        if self.savings_percentage is not None:
            data['savings_percentage'] = self.savings_percentage
        return data
    
    @classmethod
    def from_dict(cls, data):
        """Create Entry from dictionary with backward compatibility"""
        savings_percentage = data.get('savings_percentage', None)
        if savings_percentage == 0:
            savings_percentage = None
        return cls(
            job=data.get('job', '-'),
            date=data.get('date', '-'),
            description=data.get('description', '-'),
            amount=data.get('amount', 0.0),
            category=data.get('category', '-'),
            client_name=data.get('client_name', '-'),
            taxable=data.get('taxable', False),
            payment_status=data.get('payment_status', 'Pending'),
            savings_percentage=savings_percentage
        )

    def __str__(self):
        return f"{self.job} - {self.date} - {self.description} - ${self.amount}"
    
    def print(self):
        print(f"{self.job} - {self.date} - {self.description} - ${self.amount} (Taxable: {self.taxable}, Status: {self.payment_status})")