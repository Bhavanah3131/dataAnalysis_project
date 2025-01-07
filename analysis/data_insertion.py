import pandas as pd
import psycopg2
from psycopg2 import sql
from datetime import datetime
from database_setup import conn,cur
import os
from browse_files import *

#load the excel file
file_path='AlphabetAnalysis2024.xlsx'

sheet_names=['Alp081102024','Alp02082024']
# Load data from Alphabet 13F files
data_nov_08 = pd.read_excel(file_path, sheet_name='Alp081102024')
data_aug_02 = pd.read_excel(file_path, sheet_name='Alp02082024')

# Filter data for the required dates
#data_aug_02 = data_aug_02[data_aug_02['date'] == '2024-08-02']
#data_nov_08 = data_nov_08[data_nov_08['date'] == '2024-11-08']

# Combine the data
#data = pd.concat([data_nov_08, data_aug_02])

# Convert date column to datetime
#data['date'] = pd.to_datetime(data['date'])

# Insert data into  tables
def insert_data(df, transactions_nov_11):
    for index, row in df.iterrows():
        cur.execute(sql.SQL('''
        INSERT INTO {} (nameOfIssuer, titleOfClass, cusip, value, sshPrnamt, sshPrnamtType, 
        investmentDiscretion, otherManager)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING;
    ''').format(sql.Identifier(transactions_nov_11)), 
        (row['nameOfIssuer'], row['titleOfClass'], row['cusip'], row['value'], row['sshPrnamt'], 
          row['sshPrnamtType'], row['investmentDiscretion'], row['otherManager']))
        
        
insert_data(data_nov_08, 'transactions_nov_11')

insert_data(data_aug_02, 'transactions_aug_02')

conn.commit()
cur.close()
conn.close()

print("Data inserted successfully!")


