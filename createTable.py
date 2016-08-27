import psycopg2
port = 5432
constr = "dbname=testdb host=localhost port={} user=postgres".format(port)
print(constr)
conn = psycopg2.connect(constr)
print(conn)
cur = conn.cursor()
cur.execute('create table address ("ID" serial primary key, 氏名 text, フリガナ text, 種別 text, 会社名 text, 住所 text, 電話番号 text, 携帯 text, "Fax" text, "Email" text);')
conn.commit()
cur.close()
conn.close()
