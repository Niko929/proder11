

import pandas as pd



transactions = pd.read_csv("transactions.csv", sep = ";")
print(transactions)


excel_data = pd.read_excel("transactions_excel.xlsx")
print(excel_data.shape)
print(excel_data.head())