import sqlite3 

class UserManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = self.create_connection()

    def create_connection(self):
       
        # Create connection to db_file 
        
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except sqlite3.Error as e:
            print(e)
        return conn
    
    def create_tables(self): 

        """ Create tables in the SQLite database connection """

        # SQL statement for creating the UserAccounts table

        user_table_sql = """
        CREATE TABLE IF NOT EXISTS UserAccounts (
            Name VARCHAR(50) PRIMARY KEY NOT NULL,
            Password VARCHAR(100) NOT NULL
        );
        """

        # SQL statement for creating the Games table

        games_table_sql = """
        CREATE TABLE IF NOT EXISTS Games (
            GameID INTEGER PRIMARY KEY AUTOINCREMENT,
            UserName VARCHAR(100) NOT NULL,
            DatePlayed DATE NOT NULL,
            TimePlayed TIME NOT NULL,
            GamePlayed VARCHAR(500) NOT NULL,
            FOREIGN KEY (UserName) REFERENCES UserAccounts(Name)
        );
        """

        # Execute the SQL statements to create tables
        try:
            cursor = self.conn.cursor()
            cursor.execute(user_table_sql)
            cursor.execute(games_table_sql)
        except sqlite3.Error as e:
            print(e)

    def create_user(self, username, password):
        # Add user creation logic here
        pass 

    def verify_user(self, username, password):
        # Add user verification logic here
        pass

    def close_connection(self):
        self.conn.close()


if __name__ == '__main__':

    manager = UserManager('chess_app.db')

    database = "chess_app.db"

    # Create tables if no connection found 
    if manager.conn is not None:
        manager.create_tables(manager.conn)
    else:
        print("Error - couldn't create tables/connection to database")

    # End connection to save resources 
    manager.close_connection()


