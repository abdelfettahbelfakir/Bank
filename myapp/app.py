from flask import Flask, render_template, request, redirect, url_for, flash
from services.userservices import UserService
from services.compteservice import CompteService
from config import get_db_connection
from dal.userdao import UserDAO  # Import the UserDAO class

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Use UserDAO to get the database connection
        connection = get_db_connection()
        user_dao = UserDAO(connection)  # Pass the connection to UserDAO
        user_service = UserService(user_dao)  # Pass the UserDAO instance to UserService

        if user_service.authenticate_user(username, password):
            return redirect(url_for('account_management_menu'))
        else:
            flash('Invalid credentials', 'error')
    return render_template('login.html')


@app.route('/menu', methods=['GET', 'POST'])
def account_management_menu():
    if request.method == 'POST':
        choice = request.form['choice']
        
        # Using the same DB connection from the connection helper
        connection = get_db_connection()
        compte_service = CompteService(connection)
        
        if choice == '1':
            accounts = compte_service.get_all_accounts()
            return render_template('account_list.html', accounts=accounts)
        elif choice == '2':
            return render_template('search_account.html')
        elif choice == '3':
            return render_template('create_account.html')
        elif choice == '4':
            return render_template('delete_account.html')
        elif choice == '5':
            return render_template('deposit_amount.html')
        elif choice == '6':
            return render_template('withdraw_amount.html')
        elif choice == '7':
            return render_template('transfer_amount.html')
        elif choice == '8':
            return render_template('receipt.html')
        elif choice == '9':
            return "Logged out"
    return render_template('account_menu.html')


@app.route('/deposit', methods=['POST'])
def deposit():
    account_id = request.form['account_id']
    amount = float(request.form['amount'])
    connection = get_db_connection()
    compte_service = CompteService(connection)
    
    if compte_service.deposit_amount(account_id, amount):
        flash('Deposit successful!', 'success')
    else:
        flash('Error in depositing amount.', 'error')
    return redirect(url_for('account_management_menu'))


@app.route('/withdraw', methods=['POST'])
def withdraw():
    account_id = request.form['account_id']
    amount = float(request.form['amount'])
    connection = get_db_connection()
    compte_service = CompteService(connection)
    
    if compte_service.withdraw_amount(account_id, amount):
        flash('Withdrawal successful!', 'success')
    else:
        flash('Error in withdrawing amount.', 'error')
    return redirect(url_for('account_management_menu'))


@app.route('/transfer', methods=['POST'])
def transfer():
    from_account_id = request.form['from_account_id']
    to_account_id = request.form['to_account_id']
    amount = float(request.form['amount'])
    connection = get_db_connection()
    compte_service = CompteService(connection)
    
    if compte_service.transfer_amount(from_account_id, to_account_id, amount):
        flash('Transfer successful!', 'success')
    else:
        flash('Error in transferring amount.', 'error')
    return redirect(url_for('account_management_menu'))


if __name__ == '__main__':
    app.run(debug=True)
