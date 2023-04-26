from applications import app, db
from flask import render_template, redirect, url_for, flash
from applications.forms import UserDataForm
from applications.models import ShowMovies

@app.route('/')
def index():
    entries = ShowMovies.query.all()
    return render_template('index.html', entries = entries, title='Movie APP')

@app.route('/layout')
def layout():
    return render_template('layout.html', title = 'layout')

@app.route('/delete/<int:id>')
def delete(id):
    entry = ShowMovies.query.get_or_404(int(id))
    try:
        db.session.delete(entry)
        db.session.commit()
        flash('Entry deleted successfully', 'success')
        return redirect(url_for('index'))
    except:
        return "There was a problem deleting data"
    
@app.route('/add', methods=['GET', 'POST'])
def add_rating():
    form = UserDataForm()
    if form.validate_on_submit():
        entry = ShowMovies(title=form.title.data, rating=form.rating.data)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form.html', title = 'rating', form=form)