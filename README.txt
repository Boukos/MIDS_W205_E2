# MIDS_W205_E2
MIDS W205 Exercise 2

To run the application:
1.	Launch a “UCB MIDS W205 EX2-FULL” Amazon AWS instance. 
2.	Install psycopg2
3.	Install tweepy
4.	Change to w205 user
5.	Start postgres
6.	Clone github repository https://github.com/matthewpnelson/MIDS_W205_E2.git 
7.	Update Twitter Credentials in /home/w205/MIDS_W205_E2/extweetwordcount/src/spouts.tweets.py
8.	Run tweetwordcount_setup.py
9.	Navigate to /home/w205/MIDS_W205_E2/extweetwordcount
10.	Run streamparse topology (sparse run)
11.	Either:
  a.	Let run and open a new window to run query programs
    i.	finalresults.py [optional word argument]
    ii.	histogram.py [integer1, integer2]
  b.	ctrl-c to cancel streaming data collection and run query programs
    i.	finalresults.py [optional word argument]
    ii.	histogram.py [integer1, integer2]
12.	Safely shut down postgres and EC2 instance
