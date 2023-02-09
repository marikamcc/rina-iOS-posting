import sys
import psycopg2
import params
from datetime import datetime

def getinput():
    # format is based off of the script on my phone
    date = sys.argv[1]
    textarr = sys.argv[2:]
    text = " ".join(str(x) for x in textarr)
    return date, text

def writeout(new_row):
    fn = str(datetime.now().date())
    print(fn)
    f = open('/home/pi/rina/logs/'+fn+'.txt', "a")
    f.write(str(new_row)+'\n')
    f.close()


def addtodb(date,text,connectionstring):
    try:
        conn = psycopg2.connect(connectionstring, connect_timeout=3)
        # print(connectionstring)
        # print("Database connected successfully")
    except:
        # print(connectionstring)
        print("Database not connected successfully")
        sys.exit(1)

    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (title, date) VALUES (%s, %s) RETURNING *;", (text, date))
    new_row = cursor.fetchone()
    
    writeout(new_row)

    # Commit the add of post to db
    conn.commit()

    cursor.close()
    conn.close()

def main():
    date, text = getinput()
    addtodb(date, text, params.string)


if __name__ == '__main__':
    main()
