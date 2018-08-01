import mysql.connector


class DatabaseConnection:

    def __init__(self, username, password, host, database):
        self.username = username
        self.password = password
        self.host = host
        self.database = database

    def configureConnection(self):
        try:
            dbConnection = mysql.connector.connect(self.username, self.password, self.host, self.database)
        except Exception as e:
            dbConnection.close()

conn = new DatabaseConnection("eggie", "eggie", "127.0.0.1", "Market")