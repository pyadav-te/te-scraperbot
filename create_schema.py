import sqlite3

conn = sqlite3.connect('audit.db')

conn.execute('CREATE TABLE audit(report_id INTEGER PRIMARY KEY, created_by TEXT, report_name TEXT, query_date TEXT , csv_file_name TEXT)')
conn.close()
