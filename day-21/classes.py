from functools import reduce
import math

# day 21 exexercise 1
print("\nday 21 exexercise 1")
class Statistics(list):
    pass
    def count(self):
        return len(self)
    def sum(self):
        return reduce(lambda x,y: x + y,self)
    def min(self):
        self.sort()
        result = self[0]
        return result
    def max(self):
        self.sort()
        result = self[-1]
        return result
    def range(self):
        return self.max() - self.min()
    def mean(self):
        return self.sum() / self.count()
        return round()
    def median(self):
        self.sort()
        return self[self.count() // 2]
    def mode(self):
        result = {}
        for item in self:
            if(result.get(item)):
                result[item] += 1
            else: 
                result[item] = 1
        arr = list(map(lambda x: {"mode": x, "count": result[x]},result))
        arr.sort(key=lambda x: x["count"], reverse=True)
        return arr[0]
    def std(self):
        sum = 0
        mean = self.mean()
        for item in self:
            sum += math.pow(item - mean,2)
        return round(math.sqrt(sum / self.count()),1)
    def var(self):
        return round(self.std() ** 2, 1)
    def describe(self):
        print('Count:', self.count())
        print('Sum: ', self.sum())
        print('Min: ', self.min())
        print('Max: ', self.max())
        print('Range: ', self.range())
        print('Mean: ', self.mean())
        print('Median: ', self.median())
        print('Mode: ', self.mode())
        print('Standard Deviation: ', self.std())
        print('Variance: ', self.var())


        

ages = Statistics([31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26])
ages.describe()

# day 21 exexercise 2
print("\nday 21 exexercise 2")
class PersonAccount():
    def __init__(self,firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
    def total_income(self):
        return reduce(lambda x,y: x + y, self.incomes)
    def total_expense(self):
        return reduce(lambda x,y: x + y, self.expenses)
    def account_info(self):
        return f'Firstname is {self.firstname}, lastname is {self.lastname}'
    def add_income(self, income):
        self.incomes.append(income)
        return self.incomes
    def add_expense(self,expense):
        self.expenses.append(expense)
        return self.expenses
    def account_balance(self):
        return self.total_income() - self.total_expense()

person = PersonAccount('Thomas', "Partey", [100,300,500,800],[200,400])
print(person.total_income())
print(person.total_expense())
print(person.account_info())
print(person.account_balance())
print(person.add_income(1000))
print(person.account_balance())
print(person.add_expense(5000))
print(person.account_balance())

