from flask import Flask,render_template,Blueprint
from myapp.controllers.usercontroller import user_blueprint
from myapp.controllers.comptecontroller import compte_blueprint
from myapp import app
from myapp.errors.errors import register_error_handlers
import secrets
if __name__ == '__main__':
    user=app.register_blueprint(user_blueprint,url_prefix='/users')
    product=app.register_blueprint(compte_blueprint,url_prefix='/product')
    register_error_handlers(app)
    app.secret_key = secrets.token_hex(32)
    app.run(debug=True,port=8080)
    