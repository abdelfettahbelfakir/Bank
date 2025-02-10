import psycopg2
from psycopg2 import sql

class UserDAO:
    def __init__(self):
        self.db_connection = psycopg2.connect("dbname=bank_db user=postgres password=secret")

    def get_user_by_username(self, username):
        """Retourne l'utilisateur par son nom d'utilisateur"""
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username))
        user = cursor.fetchone()  # Récupère le premier résultat
        return user 

    def create_user(self, username, password_hash):
        """Crée un utilisateur avec un mot de passe haché"""
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING user_id", (username, password_hash))
        self.db_connection.commit()
        return cursor.fetchone()

    def get_user_by_id(self, user_id):
        """Récupère un utilisateur par son ID"""
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        return cursor.fetchone()
