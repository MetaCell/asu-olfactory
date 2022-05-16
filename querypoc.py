import psycopg2
import glob
import os
import csv
import time

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='asu',
    user='postgres',
    password='password'
)
cur = conn.cursor()

try:
	start = time.time()
	print("Start:")
	print(start)	
	cur.execute("""
        CREATE TABLE IF NOT EXISTS synonyms (
            CID SERIAL PRIMARY KEY,
            Synonym VARCHAR NOT NULL
        )
        """)

	# use glob to get all the csv files in the folder
	path = "CID_Chunks/"
	csv_files = glob.glob(os.path.join(path, "*.csv"))
	  
	sql_insert = """INSERT INTO synonyms(CID, Synonym)
                VALUES(%s, %s)
		ON CONFLICT (CID) DO UPDATE SET
    		(Synonym) = ROW(concat(synonyms.Synonym, ',', EXCLUDED.Synonym))"""
  
	# loop over the list of csv files
	for f in csv_files:
	    with open(f, 'r') as f1:
	       reader = csv.reader(f1)
	       next(reader) # This skips the 1st row which is the header.
	       for record in reader:
                  cur.execute(sql_insert, record)
	conn.commit()
	cur.close()
	conn.close()
	end = time.time()
	print("End Time")
	print(end - start)
except:
	print("Error")
	sys.exit()


