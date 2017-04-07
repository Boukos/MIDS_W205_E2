import sys

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# If arguement is passed at the command line, query that word & count
if len(sys.argv) == 2:

    word = sys.argv[1]

    # Connect to tcount database in postgres
    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

    # Query Results & Serve
    cur = conn.cursor()
    cur.execute("SELECT word, count FROM tweetwordcount WHERE word=%s", (word,))
    records = cur.fetchall()
    for rec in records:
       print "Total number of occurrences of {0:s}: {0:d}".format(rec[0], rec[1])
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
       print rec[0],"/t","/t","/t", rec[1]
    conn.commit()

    conn.close()
