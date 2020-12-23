from Person import Person

import pandas as pd


class PersonBuilder:

    def __init__(self):
        self.df = pd.read_csv('data.csv')
        self.consumed = self.df['consumed'].sum()
        self.paid = self.df['paid'].sum()
        self.change = self.paid - self.consumed


    def generate_person(self):

        for _, row in self.df.iterrows():

            name, consumed, paid = row.values
            change, overpaid = self.postcounts(consumed, paid)

            yield Person(name, consumed, paid, change, overpaid)


    def postcounts(self, consumed, paid):

        change = round((paid / self.paid) * self.change, 2)
        overpaid = round(paid - change - consumed, 2)

        return change, overpaid

