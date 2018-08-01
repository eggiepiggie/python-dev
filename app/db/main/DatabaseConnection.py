import mysql.connector


class DatabaseConnection:

    def __init__(self, username, password, host, database):
        self.username = username
        self.password = password
        self.host = host
        self.database = database

    def configureConnection(self):
        try:
            dbConnection = mysql.connector.connect(user = self.username, password = self.password, host = self.host, database = self.database)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            dbConnection.close()

conn = DatabaseConnection('eggie', 'eggie', '127.0.0.1', 'Market')
conn.configureConnection()
