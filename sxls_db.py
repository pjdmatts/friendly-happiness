from sqlalchemy import create_engine
import pandas as pd

#read in an excel file
df = pd.read_excel('data.xlsx', index_col=0)

#setup sqlite db
engine = create_engine('sqlite:///data.db', echo=False)

df.to_sql('data.db', con=engine, index_label='ID')


