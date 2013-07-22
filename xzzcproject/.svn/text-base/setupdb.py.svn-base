from django.http import HttpResponse
from sae.const import (MYSQL_HOST, MYSQL_HOST_S,
    MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB
)
import MySQLdb
    

def setup_db():
    # connect to database
    conn = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASS, MYSQL_DB, port=int(MYSQL_PORT))
    # select db
    conn.select_db('app_xzzc')
    # acquire cursor
    cursor = conn.cursor()
    
    try:
        metafile = open('meta/girldb.txt', 'r')
        while 1:
            line = metafile.readline()
            if not line:
                break
            str = line.split(',')
            cursor.execute("insert into gallery_girl values(%s, %s, %s)", str)
        metafile.close()
        
        metafile = open('meta/imgdb.txt', 'r')
        while 1:
            line = metafile.readline()
            if not line:
                break
            str = line.split(',')
            cursor.execute("insert into gallery_image values(%s, %s, %s)", str) 
        metafile.close()    
        res = "Setup db success"
    except IOError:
        res = "Open file error"
    # close connection
    cursor.close()
    
    return res
    

    
def setup(request):
    text = setup_db()
    return HttpResponse('<html><body>' + text + '</body></html>')


