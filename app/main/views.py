# from flask_login import login_required,current_user
# from flask import render_template,request,redirect,url_for,abort
# from ..models import User, Pitch, Comment,UpVote,DownVote
# from .forms import UpdateProfile, PitchForm
# from .. import db,photos
# from . import main
#
# #Views
# @main.route("/")
# def index():
#     """
#     View root page function that return the index page and its data
#     """
#
#     title = "Home - Welcome to my Pitch"
#     return render_template('index.html',title=title)
#
# @main.route('/user/<uname>&<id_user>')
# @login_required
# def profile(uname, id_user):
#
#     user = User.query.filter_by(username = uname).first()
#     title = f'{uname | capitalize()} profile'
#
#     get_pitches = Pitch.query.filter_by(user_id = id_user).all()
#     get_comments = Comment.query.filter_by(user_id = id_user).all()
#     get_upvotes = UpVote.query.filter_by(id_user=id_user).all()
#     get_downvotes = DownVote.query.filter_by(id_user=id_user).all()
#
#
#     if user is None:
#         abort(404)
#
#     return render_template("profile/profile.html", user = user, title = title, pitches_new = get_pitches, comments_new = get_comments)
#
# @main.route('/home', methods = ['GET', 'POST'])
# @login_required
# def home():
#     pitch_form = PitchForm()
#
#     if pitch_form.validate_on_submit():
#         pitch = pitch_form.pitch.data
#         rep = pitch_form.my_category.data
#
#         new_pitch = Pitch(pitch_content = pitch, pitch_category = rep, user = current_user)
#         new_pitch.save_pitch()
#
#         return redirect(url_for('main.home'))
#     all_pitches = pitch.get_all_pitches()
#
#     title = 'Home | One-Minute'
#     return render_template('home.html', title = title, pitch_form = pitch_form, pitches = all_pitches)
#
# @main.route('/category/<rep>')
# def category(rep):
#     my_category = Pitch.get_category(rep)
#
#     title = f"{rep} category | Tarek's Pitch"
#
#     return render_template('category.html', title=title, category=my_category)
#
#
#
#
# @main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
# def update_profile(uname):
#     user = User.query.filter_by(username = uname).first()
#     if user is None:
#         abort(404)
#
#     form = UpdateProfile()
#
#     if form.validate_on_submit():
#         user.bio = form.bio.data
#
#         db.session.add(user)
#         db.session.commit()
#
#         return redirect(url_for('.profile',uname=user.username,id_user=user_id))
#     title = 'this is the bio'
#     return render_template('profile/update.html',form=form, title=title)
#
# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))
