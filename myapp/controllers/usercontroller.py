from flask import Blueprint, render_template, request, redirect, url_for
from myapp.services.userservices import UserService

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_service = UserService()
        if user_service.authenticate_user(username, password):
            return redirect(url_for('compte.list_all_accounts'))
        else:
            return "Invalid credentials"
    return render_template('login.html')
