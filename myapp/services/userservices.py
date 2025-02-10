from myapp.dal.userdao import UserDAO
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    def __init__(self):
        # Connexion à la base de données et initialisation de l'instance DAO
        self.user_dao = UserDAO()

    def authenticate_user(self, username, password):
        """Authentifie un utilisateur avec son nom d'utilisateur et son mot de passe."""
        user = self.user_dao.get_user_by_username(username)
        
        if user and 'password' in user and check_password_hash(user['password'], password): # type: ignore
            return True
        return False

    def register_user(self, username, password):
        """Enregistre un nouvel utilisateur avec un mot de passe haché."""
        password_hash = generate_password_hash(password)
        return self.user_dao.create_user(username, password_hash)

    def get_user_by_id(self, user_id):
        """Récupère les informations d'un utilisateur par son ID."""
        return self.user_dao.get_user_by_id(user_id)

