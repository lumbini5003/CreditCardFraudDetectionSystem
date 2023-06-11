#import required libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load data
MAX_ROWs = 10000

#Load Train data
train_identity_df = pd.read_csv("../data/raw/train_identity.csv", nrows = MAX_ROWs)
train_transaction_df = pd.read_csv("../data/raw/train_transaction.csv", nrows = MAX_ROWs)

#Load Test data
test_identity_df = pd.read_csv("../data/raw/test_identity.csv", nrows = MAX_ROWs)
test_transaction_df = pd.read_csv("../data/raw/test_transaction.csv", nrows = MAX_ROWs)

#check data for transaction
train_transaction_df.head()


#there are many columns and some of them contains maximum null values, So we take some columns
trans_column = ['TransactionID','isFraud','TransactionAmt','ProductCD','card1','card2','card4','addr1','P_emaildomain','R_emaildomain', 'C1','V1']
id_column = ['id_01','id_03','id_17','id_25','DeviceType', 'DeviceInfo']

#Join Transaction and Identity dataset
train_df = df_train_trans.merge(df_train_identity, how='left', left_index=True, right_index=True)


# function to clean columns containing numerical values
def impute_median(df, column_name):
    median_value = df[~df[column_name].astype(str).str.contains('NA')][column_name].astype(float).median()
    df.loc[df[column_name].astype(str).str.contains('NA'), column_name] = median_value
    df[column_name] = df[column_name].fillna(median_value)

    return df
