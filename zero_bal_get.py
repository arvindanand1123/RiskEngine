import pandas as pd
import csv
import datetime
import numpy as np

perfCSV = pd.read_csv('perfSubset.csv',nrows=20000000)

print(perfCSV.shape)
perfCSV_columnDropped = perfCSV.drop(['monthlyReportingPeriod',
                                      'servicerName',
                                      'currIntRate',
                                      'currActualUPB',
                                      'loanAge',
                                      'remainingMonthsToLegalMaturity',
                                      'adjustedMonthsToMaturity',
                                      'maturityDate',
                                      'msa',
                                      'currLoanDelinquencyStatus',
                                      'zeroBalEffDate',
                                      'lastPaidInstallmentDate',
                                      'foreclosureDate',
                                      'dispositionDate',
                                      'foreclosureCosts',
                                      'propertyPreservationAndRepairCosts',
                                      'assetRecoveryCosts',
                                      'miscHoldingExpnAndCredits',
                                      'assocTaxesForHoldingProperty',
                                      'netSaleProceeds',
                                      'assetRecoveryCosts',
                                      'creditEnhancementProceeds',
                                      'repurchaseMakeWholeProceeds',
                                      'otherForeclosureProceeds',
                                      'nonInterestBearingUPB',
                                      'principalForgivenessAmt',
                                      'repurchaseMakeWholeProceedsFlag',
                                      'foreclosurePrincipalWriteOffAmt',
                                      'ServicingActivityIndicator',
                                      'modFlag'], axis=1)
print(perfCSV_columnDropped.shape)
print(perfCSV_columnDropped.columns.values)

perfCSV_columnRowDropped = perfCSV_columnDropped.dropna(axis=0, how="any")
print(perfCSV_columnRowDropped.shape)
acqCSV = pd.read_csv('acqSubset.csv')
print(acqCSV.columns.values)
drops = ['orginationDate','firstPaymentDate',
				'propertyState',
				'priMortgageInsurancePercent',
				'mortInsType']
acqCSV = acqCSV.drop(['orginationDate','firstPaymentDate',
				'propertyState',
				'priMortgageInsurancePercent',
				'mortInsType'],axis=1)



print(acqCSV.columns.values)
merged = pd.merge(acqCSV, perfCSV_columnRowDropped, on='loanID')
merged.dropna(axis=0, how="any")


merged[0:100].to_csv('tester.csv')
merged.to_csv('final_zero_b.csv')

