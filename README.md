# Market-Basket-Analysis


🛒 Market Basket Analysis using Apriori Algorithm (Python)
This project demonstrates Market Basket Analysis using the Apriori algorithm to uncover associations and patterns among items purchased together. Implemented in Python with mlxtend and pandas, the project analyzes a transactional dataset and extracts meaningful association rules to assist in recommendation systems or cross-sell strategies.

📌 Key Features
📊 Performs frequent itemset mining using the Apriori algorithm
✅ Supports one-hot encoding of transaction data
📈 Extracts strong association rules based on metrics like support, confidence, and lift
📁 Works with custom CSV data in a flexible format
🔍 Filters rules with lift > 1 to ensure meaningful relationships


🔧 How It Works
Read and clean the dataset by removing null entries.
Convert data into a list of transactions.
Encode transaction data using TransactionEncoder.
Apply the Apriori algorithm to find frequent itemsets with min_support=0.05.
Generate association rules with lift > 1.
Print the top rules showing:
Antecedents (If bought)
Consequents (Then likely to buy)
Support
Confidence
Lift


💡 Use Cases
📦 Retail strategy optimization
🤖 Building recommendation systems
📈 Improving cross-selling and product bundling


🛠️ Tech Stack
Python
Pandas
Mlxtend
Apriori Algorithm

