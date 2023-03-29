import sqlite3

class Database():
    
    def __init__(self, db_file):
        self.connection= sqlite3.connect(db_file)
        self.cursor= self.connection.cursor()
        
    def add_user(self, data):
        with self.connection:
            self.cursor.execute("INSERT INTO logs (user_id, username, refferer_id, refferer_username, date) " \
                                "VALUES (?, ?, ?, ?, ?)",
                                (
                                    data.get('user_id'),
                                    data.get('username'),
                                    data.get('refferer_id'),
                                    data.get('refferer_username'),
                                    data.get('date'),
                                ))
            
    def add_usermsg(self, user_id, username):
        with self.connection:
            self.cursor.execute("INSERT INTO messages (user_id, total_msg, today_msg, username) VALUES (?, ?, ?, ?)", (user_id, 1, 1, username,))
            
    def set_usermsg(self, user_id):
        with self.connection:
            self.cursor.execute("UPDATE messages SET total_msg= total_msg+1, today_msg= today_msg+1 WHERE user_id=?", (user_id, ))
    
    def reset_msg(self):
        with self.connection:
            self.cursor.execute("UPDATE messages SET today_msg= 0")
            
    def get_msg_stats(self, user_id=None):
        with self.connection:
            if user_id:
                return self.cursor.execute("SELECT * FROM messages WHERE user_id= ?", (user_id, )).fetchone()
            else:
                return self.cursor.execute("SELECT * FROM messages").fetchall()
        
    def get_invite_stats(self, user_id=None, username= None):
        with self.connection:
            if user_id or username:
                return self.cursor.execute("SELECT * FROM logs WHERE refferer_id= ? or refferer_username= ?", (user_id, username, )).fetchall()
            else:
                return self.cursor.execute("SELECT * FROM logs").fetchall()
            
    def get_invite_stats_today(self, user_id, today):
        with self.connection:
            return self.cursor.execute("SELECT * FROM logs WHERE refferer_id= ? and date > ?", (user_id, today, )).fetchall()
        
    def get_id_byUsername(self, username):
        with self.connection:
            return self.cursor.execute("SELECT user_id FROM messages WHERE username= ?", (username, )).fetchone()
        
    def reset_username(self, user_id, username):
        with self.connection:
            self.cursor.execute("UPDATE messages SET username= ? WHERE user_id = ?", (username, user_id, ))