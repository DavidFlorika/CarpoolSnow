
from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_required, current_user
from models import CarpoolPost, db

carpool_bp = Blueprint('carpool', __name__)

@carpool_bp.route('/carpool/create', methods=['GET', 'POST'])
@login_required
def create_carpool():
    if request.method == 'POST':
        post = CarpoolPost(
            user_id=current_user.id,
            resort=request.form['resort'],
            time=request.form['time'],
            pickup_location=request.form['pickup_location'],
            status='Posted'
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('carpool.view_carpools'))
    return render_template('create_carpool.html')

@carpool_bp.route('/carpool')
@login_required
def view_carpools():
    posts = CarpoolPost.query.filter_by(user_id=current_user.id).all()
    return render_template('carpools.html', posts=posts)
