from flask import Blueprint, render_template, request, redirect, url_for
from services.compteservice import CompteService

compte_blueprint = Blueprint('compte', __name__)

@compte_blueprint.route('/accounts')
def list_all_accounts():
    compte_service = CompteService()
    accounts = compte_service.get_all_accounts()
    return render_template('index.html', accounts=accounts)

@compte_blueprint.route('/account/<int:id>')
def search_account(id):
    compte_service = CompteService()
    account = compte_service.search_account(id)
    if account:
        return render_template('account_details.html', account=account)
    return "Account not found"

@compte_blueprint.route('/create_account', methods=['POST'])
def create_account():
    balance = request.form['balance']
    account_type = request.form['account_type']
    compte_service = CompteService()
    compte_service.create_account(account_type, float(balance))
    return redirect(url_for('compte.list_all_accounts'))
