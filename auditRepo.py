import sqlite3 as sql

def save(username, report, date, fileName):
    with sql.connect("audit.db") as con:
        cur = con.cursor()
        data = (username,report, date,fileName)
        cur.execute("INSERT INTO audit (created_by,report_name,query_date,csv_file_name) VALUES (?, ?, ?, ?)", data)
        con.commit()

def getAll():
    con = sql.connect("audit.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from audit")
    users = cur.fetchall()
    return users

