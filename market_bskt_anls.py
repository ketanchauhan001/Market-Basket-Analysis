from mlxtend.preprocessing.transactionencoder import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd


# Read CSV
data = pd.read_csv(r"C:\Users\ketan\ketan_python\csv files\Market_Basket_Optimisation.csv")

# Remove NaN values and create transactions list
market=[]
for i in range(0,len(data)):
    temp=[]
    for j in data.columns:
        if(type(data[j][i])==str):
            temp.append(data[j][i])
    market.append(temp)

# One-hot encoding
tr = TransactionEncoder()
df_encoded = pd.DataFrame(tr.fit_transform(market), columns=tr.columns_)

# Apply Apriori Algorithm
model = apriori(df_encoded, min_support=0.05, use_colnames=True, max_len=3)

# Generate Association Rules
rules = association_rules(model, metric="lift", min_threshold=1)

# Print Association Rules
print("\nTop Association Rules:\n")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

