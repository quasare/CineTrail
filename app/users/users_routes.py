from flask import Blueprint, render_template, jsonify


user = Blueprint('user', __name__, template_folder='templates',
                     static_folder='static')

@user.route('/')
def user_dashboard():
    return render_template('user_dashboard.html')