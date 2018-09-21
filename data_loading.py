import pandas as pd 


def load(path):
	"""
	Reads historical production data based on file path in 
	config file

	@retuns: df with 9 columns:
	[day, month, year, week_number,slab_production,pickeld_production,
	galvanized_1_production, galvanized_2_production,galvanized_3_production]
	"""
	df = pd.read_excel(path)
	return df