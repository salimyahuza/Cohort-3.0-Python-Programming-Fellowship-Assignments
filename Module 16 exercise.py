# This is a class called Statistics that includes methods to calculate various statistical measures
import statistics
from collections import Counter

class Statistics:
    def __init__(self, data):
        self.data = data
    
    def count(self):
        return len(self.data)
    
    def sum(self):
        return sum(self.data)
    
    def min(self):
        return min(self.data)
    
    def max(self):
        return max(self.data)
    
    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return statistics.mean(self.data)
    
    def median(self):
        return statistics.median(self.data)
    
    def mode(self):
        mode_data = Counter(self.data).most_common(1)[0]
        return {'mode': mode_data[0], 'count': mode_data[1]}
    
    def std(self):
        return statistics.stdev(self.data)
    
    def var(self):
        return statistics.variance(self.data)
    
    def freq_dist(self):
        freq_distribution = Counter(self.data).items()
        freq_distribution = sorted(freq_distribution, key=lambda x: x[1], reverse=True)
        total_count = self.count()
        freq_distribution = [(count / total_count * 100, value) for value, count in freq_distribution]
        return freq_distribution
    
    def describe(self):
        description = {
            'Count': self.count(),
            'Sum': self.sum(),
            'Min': self.min(),
            'Max': self.max(),
            'Range': self.range(),
            'Mean': self.mean(),
            'Median': self.median(),
            'Mode': self.mode(),
            'Variance': self.var(),
            'Standard Deviation': self.std(),
            'Frequency Distribution': self.freq_dist()
        }
        return description

# Example usage:
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 29.76
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.27
print('Variance: ', data.var()) # 18.27
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 31), (8.0, 34), (8.0, 37), (8.0, 24), (8.0, 33), (4.0, 25), (4.0, 38), (4.0, 29)]

# Describe the data
description = data.describe()
for key, value in description.items():
    print(f"{key}: {value}")

# Level two exercise
# This is a class called PersonAccount that includes specified properties and methods
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, description):
        self.incomes.append({'amount': amount, 'description': description})

    def add_expense(self, amount, description):
        self.expenses.append({'amount': amount, 'description': description})

    def total_income(self):
        return sum(income['amount'] for income in self.incomes)

    def total_expense(self):
        return sum(expense['amount'] for expense in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'total_income': self.total_income(),
            'total_expense': self.total_expense(),
            'account_balance': self.account_balance()
        }

# Example usage:
person = PersonAccount('John', 'Doe')
person.add_income(5000, 'Salary')
person.add_income(200, 'Freelance')
person.add_expense(1500, 'Rent')
person.add_expense(200, 'Groceries')

print(person.account_info())
