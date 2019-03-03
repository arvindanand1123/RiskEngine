import pandas as pd
import math

acq_n = 3652611
perf_n = 145328640
acq_data = pd.read_csv('acqSubset.csv',nrows=3652611)
print(acq_data.shape)
perf_data = pd.read_csv('perfSubset.csv',nrows=3652611)
print(perf_data.shape)

merged_data = acq_data.merge(perf_data, how='left', left_on='loanID',  right_on='loanID')
print(merged_data.shape)


drop_columns = ['originationDate','firstPaymentData',
				'propertyState',
				'priMortgageInsurancePercent',
				'mortInsType',
				'monthlyReportingPeriod',
				'currIntRate',
				'loanAge',
				'msa',
				'modFlag',
				'zeroBalEffDate',
				'repurchaseMakeWholeProceedsFlag']
print(merged_data['currLoanDelinquencyStatus'][0:10])

drop_indexes = []
y_count = 0;


map_values = {}

new_merged = merged_data.dropna(axis=1,how='all',thresh=1000000)
print(new_merged.shape)
new_merged = new_merged.dropna(axis=0,how='any')
print(new_merged.shape)
#print(new_merged['currLoanDelinquencyStatus'])
#print(new_merged['currLoanDelinquencyStatus'][0:10])

print(new_merged.shape)
#print(new_merged['currLoanDelinquencyStatus'])
print(new_merged['currLoanDelinquencyStatus'][0:10])


'''

print(y_count)
maybe_drops = merged_data.columns

maybe_counts = [0] * len(maybe_drops)
maybe_dict = dict(zip(maybe_drops,maybe_counts))

found_value = False
for col in merged_data.columns:
	found_value = False
	for val in merged_data:
		try:
			if(not math.isnan(val)):
				found_value = True
			if(not val):
				found_value = True
		except: 
			continue
	maybe_dict[col] = found_value
'''

y = []
y_column = 'zeroBalCode'


'''
for col in merged_data.columns:
	if(col == y_column):
		for val in merged_data[col]:
			if(not math.isnan(val)):
				y.append(val)
			else:
				del 

'''
new_merged.to_csv('merge_final_w_zeroBal.csv')
new_merged[0:1000].to_csv('final_sample_w_ZERO1000.csv')


merge_sample2000 = pd.read_csv('merge_final.csv')
print(merge_sample2000.shape)
map_values = {'X':float('nan'),0:0}
print(merge_sample2000[0:10])



merge_sample2000.loc[merge_sample2000.currLoanDelinquencyStatus == 'X', 'currLoanDelinquencyStatus'] = float('nan')
'''for i in merge_sample2000['currLoanDelinquencyStatus']:
	print(type(i))


merge_sample2000['currLoanDeliquencyStatus'] = merge_sample2000['currLoanDelinquencyStatus'].map(map_values)
print(merge_sample2000[0:10])
'''
new_merged = merge_sample2000.dropna(axis=0,how='any')
print(new_merged.shape)
new_merged.to_csv('merge_final.csv')
merge_sample2000 = new_merged[0:1000] 
#merge_sample2000 = merge_sample2000.drop('X',axis=1)
merge_sample2000.to_csv('final_sample1000.csv')

'''
indexes = []
for i in merge_sample2000['currLoanDelinquencyStatus']:
	if(i == 'X'):
		print(True)
		i = float('nan')
w.loc[w.female != 'female', 'female'] = 0
w.loc[w.female == 'female', 'female'] = 1

'''


