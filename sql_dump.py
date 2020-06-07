import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy

engine = sqlalchemy.create_engine("%s://%s:%s@%s:%s/%s" % (
    "mysql+pymysql",
    "congress_admin",
    "password",
    "ip",
    port,
    "ds_data"
))
def truncate_before_dump(table):
   '''
   To Truncate all tables before populating them
   '''
   global engine
   with engine.connect() as con:
       print("Deleting %s table from %s" % (table, 'kg_builder_test'))
       con.execute("DELETE FROM " + table + ";")
       
       
def dump_to_sql(dump_df, relationship):
   '''
   Uses pandas.to_sql to dump directly into the DB
   '''
   global engine
   dump_df.to_sql(name=relationship, con=engine, if_exists='append', index=False, chunksize=1000)
   