import sys

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# If no arguement is passed at the command line, exit script
if len(sys.argv) != 2:
    print "Please provide a word argument to query."
    exit(1)


# Connect to tcount database in postgres
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

# Query Results & Serve
cur = conn.cursor()
cur.execute("SELECT word, count from tweetwordcount")
records = cur.fetchall()
for rec in records:
   print "word = ", rec[0]
   print "count = ", rec[1], "\n"
conn.commit()

conn.close()
