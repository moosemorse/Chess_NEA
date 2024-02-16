import sqlite3 
import bcrypt 

class UserManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = self.create_connection()
        self.cursor = self.conn.cursor()

    def create_connection(self):
       
        # Create connection to db_file 
        
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
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
            self.cursor.execute(user_table_sql)
            self.cursor.execute(games_table_sql)
            # Commit all changes to the database 
            self.conn.commit() 
        except sqlite3.Error as e:
            print(e)

    def hash_password(self, password): 
        # Hash a password 
        salt = bcrypt.gensalt() 
        return bcrypt.hashpw(password.encode('utf-8'), salt) 
    
    def verify_password(self, stored_password, provided_password):
        # Check password input with stored password in database 
        return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password)

    def create_user(self, username, password):
        try:
            hashed_password = self.hash_password(password)
            # Create new row with username and their hashed password in table users 
            self.cursor.execute('INSERT INTO UserAccounts (Name, Password) VALUES (?, ?)', (username, hashed_password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            # Integrity error means that user is already on database, so return False 
            return False 
        
    def login(self, username, password):
        # Obtain password from database 
        self.cursor.execute('SELECT Password FROM UserAccounts WHERE Name=?', (username,))
        result = self.cursor.fetchone()
        if result and self.verify_password(result[0], password):
            return True
        # Passwords didn't match or user account not found 
        return False 
    
    def save_game(self, history): 
        
        # SQL statement for inserting a new game record
        insert_game_sql = '''
        INSERT INTO Games (UserName, DatePlayed, TimePlayed, GamePlayed, outcome, result)
        VALUES (?, ?, ?, ?, ?, ?)
        '''

        # Execute the SQL statement
        try:
            self.cursor.execute(insert_game_sql, (history['username'], history['date'], history['time'], history['pgn'], 
                                                  history['outcome'], history['reason']))
            self.conn.commit()
            return True
        # Prevent program crashing 
        except sqlite3.Error as e:
            print(e)
            return False

    def close_connection(self):
        self.conn.close()

    def check_tables(self): 
        cursor = self.conn.cursor() 
        # Retrieve list of all tables in database 
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        # Print the list of tables
        for table in tables:
            print(table)


if __name__ == '__main__':

    database = "chess_app.db"

    manager = UserManager(database)
         
    # End connection to save resources 
    manager.close_connection()


