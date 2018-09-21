import pandas as pd 


def load(path = './IONIZATION_case_daily_production_data.xlsx'):
	
	df = pd.read_excel(path)
	return df