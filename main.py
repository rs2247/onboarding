import pandas as pd 
import data_loading
import model


if __name__ == '__main__':

	data = data_loading.load()
	model.capacity_prediction(data)