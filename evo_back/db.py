import sqlite3

con = sqlite3.connect("evo.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

#query = "INSERT INTO sys_command VALUES(null, 'steam', 'C:\\Program Files (x86)\\Steam\\steam.exe')"
#cursor.execute(query)
#con.commit()

#query = "DELETE FROM sys_command WHERE id = 2 "
#cursor.execute(query)
#con.commit()

#query = "UPDATE sys_command SET id = 3 WHERE id = 4"
#cursor.execute(query)
#con.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

#query = "INSERT INTO web_command VALUES(null, 'gemini', 'https://gemini.google.com/')"
#cursor.execute(query)
#con.commit()
