import pandas as pd
from sqlalchemy import create_engine

df=pd.read_parquet("matches_analyzed_epl2023.parquet")
print(df.dtypes)

#Connect to postgres
engine = create_engine("postgresql+psycopg2://postgres:PAUL081eru%40%40@localhost:5432/epl20_23")

df.to_sql("matches",engine, if_exists="replace",index=False)
