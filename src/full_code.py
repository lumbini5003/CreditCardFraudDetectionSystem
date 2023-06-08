import numpy as np # linear algebra
import pandas as pd # data processing

MAX_ROWs = 10000

#Load Train data
train_identity_df = pd.read_csv("/data/raw/train_identity.csv", nrows = MAX_ROWs)
train_transaction_df = pd.read_csv("/data/raw/train_transaction.csv", nrows = MAX_ROWs)

#Check data
train_identity_df.head()
