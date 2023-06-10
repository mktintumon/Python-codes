import sqlite3

# connection to the SQLite db
conn = sqlite3.connect('world.db')
cursor = conn.cursor()

# query to select the top 1000 cities ordered by population
query = "SELECT ID, Name, Population FROM City ORDER BY Population DESC LIMIT 1000"
cursor.execute(query)

# Fetching all the rows 
data = cursor.fetchall()

for row in data:
    city_id, city_name, population = row
    print(f"City ID: {city_id}, Name: {city_name}, Population: {population}")


# Exit point
conn.commit()
cursor.close()
conn.close()