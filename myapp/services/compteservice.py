from dal.comptedao import CompteDAO
from psycopg2 import connect

class CompteService:
    def __init__(self):
        self.db_connection = connect("dbname=bank_db user=postgres password=secret")
        self.compte_dao = CompteDAO(self.db_connection)

    def get_all_accounts(self):
        return self.compte_dao.get_all_accounts()

    def search_account(self, account_id):
        return self.compte_dao.get_account_by_id(account_id)

    def create_account(self, account_type, balance):
        return self.compte_dao.create_account(balance, account_type)

    def delete_account(self, account_id):
        self.compte_dao.delete_account(account_id)
