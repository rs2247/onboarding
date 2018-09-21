import pandas as pd

def capacity_prediction(data):
	"""
	Based on historical data, forecasts the
	production for the next 6 months for 3 assets: 
		slab,
		picking line,
		galvanizing line
	
	@param data: df with daily production 
	@return: df with 3 columns with capacity predictions
	 		 and 6 rows, one for each month
	"""
