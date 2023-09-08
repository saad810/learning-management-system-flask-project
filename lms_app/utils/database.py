import mysql.connector

class DBconnector:
    def __init__(self) -> None:
        self.db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "saad2002",
            database = "lmsdb"
        )
        self.cursor = self.db.cursor()

    def execute_query(self,query, params = None):
        self.cursor.execute(query, params)
        self.db.commit()
        return self.cursor.fetchall()
    
    def execute_NoCommit(self,query, params = None):
        self.cursor.execute(query,params)
        return self.cursor.fetchall()
    
    
    def close_connection(self):
        self.cursor.close()
        self.db.close()
