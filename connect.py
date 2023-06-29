import sqlite3
import pandas as pd


#read csv file

df = pd.read_csv('/data/100M_Male.csv')

conn = sqlite3.connect('sprinters.db')

c = conn.cursor()


# create table
c.execute("""CREATE TABLE sprinters (
            rank integer,
            mark text,
            wind text,
            name text,
            nat text
            )""")



# commit our command
conn.commit()


# close our connection
conn.close()


# read from csv

df.to_sql('sprinters', conn, if_exists='replace', index = False)
