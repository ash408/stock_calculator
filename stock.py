

class Stock:

	def __init__(self, mark):
		self.mark = mark

	def change_mark(self, amount):
		self.mark += amount


class Position:

	def __init__(self, purchace_mark):
		self.purchace_mark = purchace_mark

	def calculate_profit_mark(percentage):
		percent_mark = self.purchace_mark / 100
		required_percentage = percent_mark * percentage

		return self.purchace_mark + required_percentage
