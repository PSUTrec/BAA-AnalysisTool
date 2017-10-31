import psycopg2
import csv
from IPython.core.display import display, HTML 
from settings import DBNAME, DBPASS, DBUSER, DBHOST

def db_connect():
    conn = None
    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (DBNAME,DBUSER,DBHOST,DBPASS))
    except:
        print ("Unable to connect to the database")
        
    return conn

def get_querydata(qsql):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute(qsql)
    colnames = [desc[0] for desc in cur.description]
    print(colnames)
    rows = cur.fetchall()
    for row in rows:
        print (row) 
    cursor.close()
    connection.close()        
        
def query2csv(qsql, csvfile):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute(qsql)   
    colnames = [desc[0] for desc in cur.description]
    with open(csvfile, 'w', newline='') as csvfhandle:
        csvwriter = csv.writer(csvfhandle, delimiter='\t',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(colnames)
        rows = cur.fetchall()
        for row in rows:
            csvwriter.writerow(row)
    cur.close()
    conn.close()
    display(HTML("<h1>Result</h1><a href='./%s?download=1' target='_blank'>%s</a>" % (csvfile, csvfile)))