"""
dbio.py
"""
import pymysql
import cryptography
import time
import databaseconfig as cfg


class DbIO:
    def __init__(self):
        # Setup connection to DB
        self.db = pymysql.connect(host=cfg.mysql["host"], user=cfg.mysql["user"], password=cfg.mysql["passwd"], db=cfg.mysql["db"])

        # Establish DB cursor used for write/read activities
        self.cursor = self.db.cursor()

        # ID needs to be removed. This is a temp measure to have unique private keys.
        self.id = 0;
        print('dbio object created');

    def write_datapoint_record(self, ticker, sentiment, text):
        # fix the use of id here. I want this to be taken care of by the DB itself.
        # Prepare sql query to insert a new data point.
        sql = "INSERT INTO datapoint(ID, TICKER, DATE, SENTIMENT, TEXT) " \
              "VALUES ('%d', '%s', '%s', '%d', '%s' )" % \
              (self.id, ticker, time.strftime('%Y-%m-%d %H:%M:%S'), sentiment, text)
        try:

            self.cursor.execute(sql)
            self.db.commit()
            self.id += 1
        except:
            self.db.rollback()
            print("Error: db rolled back")

    def read_datapoint_record(self, id):
        sql = "SELECT * FROM datapoint WHERE id = '%d'" % (id)

        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                id = row[0]
                ticker = row[1]
                date = row[2]
                sentiment = row[3]
                text = row[4]
                #print("id: %d, ticker: %s, date: %s, sentiment: %d, text: %s" %
                #     (id, ticker, date, sentiment, text))
        except:
            print("Error: unable to fetch data")

    def __del__(self):
        self.db.close()
