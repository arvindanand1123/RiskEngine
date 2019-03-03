import pandas as pd
import csv
import datetime

perfCSV = pd.read_csv('perfSubset.csv', nrows=6000000)
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
                                      'zeroBalEffDate',
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
