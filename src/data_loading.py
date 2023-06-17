#Load data
MAX_ROWs = 10000

#Load Train data
train_identity_df = pd.read_csv("../data/raw/train_identity.csv", nrows = MAX_ROWs)
train_transaction_df = pd.read_csv("../data/raw/train_transaction.csv", nrows = MAX_ROWs)

#Load Test data
test_identity_df = pd.read_csv("../data/raw/test_identity.csv", nrows = MAX_ROWs)
test_transaction_df = pd.read_csv("../data/raw/test_transaction.csv", nrows = MAX_ROWs)
