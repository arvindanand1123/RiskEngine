import pandas as pd
import math

acq_data = pd.read_csv('acqSubset.csv')
perf_data = pd.read_csv('perfSubset.csv')

merged_data = pd.merge(acq_data, perf_data)



drop_columns = ['originationDate','firstPaymentData',
				'propertyState',
				'priMortgageInsurancePercent',
				'mortInsType']
print(merged_data.shape)
'''
for col in merged_data.columns:
	if(col in drop_columns):
		del merged_data[col]


y = []
y_column = 'zeroBalCode'

for col in merged_data.columns:
	if(col == y_column):
		for val in merged_data[col]:
			if(not math.isnan(val)):
				print(val)
				#y.append(val)
'''
#merged_data.to_csv('sample_merge_csv.csv')
