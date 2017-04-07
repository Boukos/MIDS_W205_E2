# Serving Python script to query the tweetwordcount table in postgres.
# Provides the word and word count of all words with a count within the bounds
# of two integers passed as arguments at the command line in the form [int1,int2].
# Sorted by highest to lowest count.

import sys

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# If no arguement is passed at the command line, exit script
if len(sys.argv) != 2:
    print "Please provide an argument in the form [int,int] to query."
    exit(1)

user_input = sys.argv[1].split(",")
k1,k2 = int(user_input[0]), int(user_input[1])

# Connect to tcount database in postgres
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

# Query Results & Serve
cur = conn.cursor()
cur.execute("SELECT word, count from tweetwordcount WHERE count>=%s AND count<=%s \
    ORDER BY count DESC", (k1,k2))
records = cur.fetchall()
for rec in records:
   print "{0:s}: {1:d}".format(rec[0],rec[1])
conn.commit()

conn.close()
