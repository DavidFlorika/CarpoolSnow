
from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/account')
@login_required
def account():
    return render_template('account.html', user=current_user)

@main_bp.route('/about')
def about():
    return render_template('about.html')
