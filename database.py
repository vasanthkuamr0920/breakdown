
import mysql.connector


# Returns the current local date


mydb = mysql.connector.connect(
  host="sql12.freemysqlhosting.net",
  user="sql12756460",
  password="Grf9YZ5Ta3",
  database="sql12756460"
)

mycursor = mydb.cursor()
mycursor.execute('''CREATE TABLE if not exists Ele_log(Date date, MachineName TEXT,Department TEXT, ItemNo TEXT ,Start_time TEXT, End_time TEXT,
                NaturBreakdown TEXT,Details  TEXT,Attendby TEXT,UsedSpares TEXT ,
                Remarks TEXT,Duration float);''')
print(mydb)
mycursor.execute("SELECT COUNT(*) FROM Ele_log")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)





def insert_fun(data):
        try:
                mydb = mysql.connector.connect(
                host="sql12.freemysqlhosting.net",
                user="sql12756460",
                password="Grf9YZ5Ta3",
                database="sql12756460"
                                        )
        
                mycursor = mydb.cursor()
        
                sql = """INSERT INTO Ele_log (Date, MachineName ,Department , ItemNo  ,Start_time , End_time ,NaturBreakdown ,Details  ,
                        Attendby ,UsedSpares  ,Remarks ,Duration ) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"""
                val = (data)
                mycursor.execute(sql, val)

                mydb.commit()

                mycursor.close()
                return "success"

        except:
                pass

