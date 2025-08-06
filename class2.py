class Account():
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
  def credit(self, amount):
    self.balance += amount
    # Write in the live db
  def debit (self, amount):
    self.balance -= amount
    # write in to the live DB

roopesh_ac = Account("roopesh", 5000)
lokesh_ac = Account("lokesh", 10000)

roopesh_ac.debit(1000)
lokesh_ac.credit(1000)

print(roopesh_ac.balance)
print(lokesh_ac.balance)