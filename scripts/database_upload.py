import pandas as pd
from sqlalchemy import create_engine

# Load cleaned dataset
df = pd.read_csv("data/cleaned_currency_data.csv")

# MySQL connection
engine = create_engine(
    "mysql+pymysql://root:root@localhost/financial_dashboard"
)

# Upload dataset
df.to_sql(
    "currency_data",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data uploaded successfully!")