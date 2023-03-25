class CreditCard:
	"""A consumer credit card."""

	def __init__(self, customer, bank, acnt, limit):
		"""Create a new credit card instance.

		The initial balance is zero.

		customer the name of the customer (e.g., 'John Bownman')
		bank 	 the name of the bank (e.g., 'California Savings')
		acnt 	 the account identifier (e.g., '5391 0375 9387 5309')
		limit    credit limit (measured in dollars)
		"""

		self._customer = customer
		self._bank = bank
		self._account = acnt
		self._limit = limit
		self._balance = 0

	def get_customer(self):
		"""Return name of the customer."""
		return self._customer

	def get_bank(self):
		"""Return bank's name."""
		return self._bank

	def get_account(self):
		"""Return the card identying number (typicalle stored as a string)."""
		return self._account

	def get_limit(self):
		"""Return current credit limit."""
		return self._limit

	def get_balance(self):
		"""Return current balance."""
		return self._balance

	def charge(self, price):
		"""Charge given price to the card, assuming sufficient credit limit.

		Return True if charge was processed; False if charge was denied.
		"""
		if price + self._balance > self._limit:
			return False
		else:
			self._balance += price
			return True

	def make_payment(self, amount):
		"""Process customer payment that reduces balance."""
		self._balance -= amount

if __name__ == '__main__':
	data = CreditCard('D.P.', 'BS', '1', 50)
	print(data.get_balance())