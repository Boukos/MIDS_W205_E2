# Serving Python script to query the tweetwordcount table in postgres.
# Provides the count of a single word if that word is provided as an argument
# at the command line, otherwise it will print out all words in alphebetical
# order with each words corresponding count at the time of query.

import sys

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# If argument is passed at the command line, query that word & count
if len(sys.argv) == 2:

    word = sys.argv[1]

    # Connect to tcount database in postgres
    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

    # Query Results & Serve
    cur = conn.cursor()
    cur.execute("SELECT word, count FROM tweetwordcount WHERE word=%s", (word,))
    records = cur.fetchall()
    for rec in records:
       print "Total number of occurrences of '{0:s}': {1:d}".format(rec[0], rec[1])
    conn.commit()

    conn.close()

# If no argument provided, serve all results alphebetically & one word per line
else:
    # Connect to tcount database in postgres
    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

    # Query Results & Serve
    cur = conn.cursor()
    cur.execute("SELECT word, count FROM tweetwordcount ORDER BY word ASC")
    records = cur.fetchall()
    for rec in records:
       print rec[0], rec[1]
    conn.commit()

    conn.close()
