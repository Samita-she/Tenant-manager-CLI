class Tenant:
    def __init__(self, tenant_id, name, unit_number, move_in_date, move_out_date=None):
        self.tenant_id = tenant_id
        self.name = name
        self.unit_number = unit_number
        self.move_in_date = move_in_date
        self.move_out_date = move_out_date

    def to_dict(self):
        return self.__dict__

class Payment:
    def __init__(self, tenant_id, amount, date):
        self.tenant_id = tenant_id
        self.amount = amount
        self.date = date

    def to_dict(self):
        return self.__dict__
