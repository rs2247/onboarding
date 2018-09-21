import pandas as pd 


def load(path: str = './IONIZATION_case_daily_production_data.xlsx') -> pd.DataFrame:
	"""
	Reading the data from file
	:param path: path to read from
	:return: DataFrame
	"""
	df = pd.read_excel(path)
	return df