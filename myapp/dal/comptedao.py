import psycopg2
from psycopg2 import sql

class CompteDAO:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_all_accounts(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM accounts ORDER BY balance DESC")
        return cursor.fetchall()

    def get_account_by_id(self, account_id):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM accounts WHERE account_id = %s", (account_id,))
        return cursor.fetchone()

    def create_account(self, balance, account_type):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO accounts (balance, account_type) VALUES (%s, %s) RETURNING account_id", (balance, account_type))
        self.db_connection.commit()
        return cursor.fetchone()

    def delete_account(self, account_id):
        cursor = self.db_connection.cursor()
        cursor.execute("DELETE FROM accounts WHERE account_id = %s", (account_id,))
        self.db_connection.commit()
    def update_account_balance(self, account_id, new_balance):
        cursor = self.db_connection.cursor()
        """Met à jour le solde d'un compte dans la base de données."""
        try:
            # Exécuter la requête SQL pour mettre à jour le solde
            update_query = """
                UPDATE accounts 
                SET balance = %s 
                WHERE id = %s;
            """
            cursor.execute(update_query, (new_balance, account_id))
            self.db_connection.commit()  # Appliquer les modifications
        except Exception as e:
            self.db_connection.rollback()  # Annuler en cas d'erreur
            print(f"Erreur lors de la mise à jour du solde du compte {account_id}: {e}")
        finally:
            cursor.close()
