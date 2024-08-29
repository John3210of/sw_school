import mysql.connector

'''
sql에서의 transaction 과정을 python으로 옮겨 보기
'''

conn = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="test_db"
)
cursor = conn.cursor()

try:
    conn.start_transaction()
    cursor.execute("INSERT INTO tcity (name, area, popu, metro, region) VALUES ('CityA', 100, 1000, 'MetroA', 'RegionA')")
    conn.savepoint("savepoint1")
    cursor.execute("INSERT INTO tcity (name, area, popu, metro, region) VALUES ('CityB', 'InvalidAreaValue', 2000, 'MetroB', 'RegionB')")
    conn.commit()
    print("Transaction committed successfully")
except mysql.connector.Error as err:
    print(f"Error occurred: {err}")
    conn.rollback("savepoint1")
    print("Rolled back to savepoint1")
    conn.commit()
    print("Transaction after rollback committed successfully")
finally:
    # 연결 닫기
    cursor.close()
    conn.close()
