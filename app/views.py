# -*- coding: utf-8 -*-
"""
    app.views
    ~~~~~~~~~~~

    Views for pre-registration

    :author: Adam Zucker
    :copyright: (c) 2013 by Hallspot.
"""
import os
from flask import render_template, jsonify, request, flash, redirect, session, url_for, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from werkzeug import secure_filename

from app import app, models, db, lm
from models import User
from forms import PostForm, LoginForm, RegisterForm



@app.route('/')
def home():
    posts = db.session.query(models.Post).all()
    posts.reverse()
    user = db.session.query(models.User).filter("users.id="+str(session['user_id'])).first()
    return render_template('index.html', posts=posts, user=user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    # if user is not None and user.is_authenticated():
    #     return redirect(url_for('admin'))
    form = LoginForm()
    #import pdb;pdb.set_trace()
    if form.validate_on_submit():
        user = form.get_user()
        session['remember_me'] = form.remember_me.data
        login_user(user, remember=True)
        return redirect('/admin')
    return render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/admin', methods = ['GET', 'POST'])
@login_required
def admin():
    form = PostForm()
    if request.method == 'POST':
        flash('Created post '+str(form.title.data))

        #import pdb;pdb.set_trace()
        image = request.files['image']
        if image:
            filename = secure_filename(image.filename)
            image.save("".join([os.getcwd(),"/app", app.config['UPLOAD_FOLDER'],"/", filename]))

        new_post = models.Post(body=form.body.data, 
                                   title=form.title.data,
                                   link=form.link.data,
                                   user_id=session['user_id'],
                                   picture=filename)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/')
    return render_template('admin.html', form=form)


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))



