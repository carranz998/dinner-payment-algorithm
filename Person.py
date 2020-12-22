class Person:

    def __init__(self, name, consumed, paid):
        self.name = name
        self.consumed = consumed
        self.paid = paid
        self.change = 0
        self.overpaid = 0

    def __str__(self):
        return self.name + " " + str(self.consumed) + " " + str(self.paid) + " " + str(self.change) + " " + str(self.overpaid)

    def calcule_change(self, total_consumed, total_paid):
        self.change = (self.paid / total_paid) * (total_paid - total_consumed)   

    def calcule_overpaid(self):
        self.overpaid = self.paid - self.change - self.consumed
