from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_app.models.show import Show
from flask_app.models.like import Like

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    all_shows = Show.get_all()
    logged_user = User.get_by_id({'id' : session['user_id']})
    liked_shows_id = Like.get_shows_id_for_user({'id' : session['user_id']})
    user_likes = Like.count_for_user({'user_id' : session['user_id']})
    return render_template("dashboard.html", all_shows = all_shows, user = logged_user, liked_shows_id = liked_shows_id, user_likes=user_likes)

@app.route('/shows/new')
def new_show():
    if 'user_id' in session:
        return render_template('new_show.html')
    return redirect('/')

@app.route('/my_shows')
def show_shows():
    if 'user_id' in session:
        all_shows = Show.get_shows_by_user({'user_id' : session['user_id']})
        logged_user = User.get_by_id({'id':session['user_id']})
        return render_template('my_shows.html', all_shows = all_shows, user = logged_user)
    return redirect('/')

@app.route('/shows/create', methods = ['POST'])
def create_show():
    if not Show.validate(request.form):
        return redirect('/shows/new')
    data = {
        **request.form, 'user_id' : session['user_id']
    }
    Show.create(data)
    return redirect ('/dashboard')

@app.route('/shows/<int:show_id>')
def show_show(show_id):
    if 'user_id' in session:
        show = Show.get_by_id({'id' : show_id})
        creator = User.get_by_id({'id' : show.user_id})
        likes = Like.count_for_show({'show_id' : show_id})
        return render_template('view_show.html', show = show, user = creator, likes = likes)
    return redirect('/')

@app.route('/shows/<int:show_id>/edit')
def edit_show(show_id):
    if 'user_id' in session:
        show = Show.get_by_id({'id' : show_id})
        if show:
            if show.user_id == session['user_id'] :
                return render_template('edit_show.html', show = show)
            else :
                hacker = User.get_by_id({'id' : session['user_id']})
                if hacker.warning<1 : #TRUE MEANS IT'S HIS FIRST TIME
                    User.add_warning({'id' : session['user_id']}) #ADD A WARNING
                    ip_address = request.remote_addr
                    return render_template('gotcha.html', hacker=hacker, show_id = show_id, ip_address=ip_address)
                #LOGOUT THE HACKER
                return redirect('/logout')
        else :
            return render_template('404.html')
    return redirect('/')

@app.route('/shows/<int:show_id>/update', methods = ['POST'])
def update_show(show_id):
    if not Show.validate(request.form):
        return redirect(f'/shows/{show_id}/edit')
    data = {
        **request.form, 'user_id' : session['user_id'], 'id' : show_id
        }
    Show.update(data)
    return redirect ('/dashboard')

@app.route('/shows/<int:show_id>/delete')
def delete_show(show_id):
    if 'user_id' in session:
        show_to_delete = Show.get_by_id({'id' : show_id})
        if show_to_delete:
            if show_to_delete.user_id == session['user_id'] :
                Like.delete({'show_id' : show_id})
                Show.delete({'id' : show_id})
                return redirect('/dashboard')
            hacker = User.get_by_id({'id' : session['user_id']})
            if hacker.warning<1 : #TRUE MEANS IT'S HIS FIRST TIME
                User.add_warning({'id' : session['user_id']}) #ADD A WARNING
                ip_address = request.remote_addr
                return render_template('gotcha.html', hacker=hacker, show_id = show_id, ip_address=ip_address)
            #LOGOUT THE HACKER
            return redirect('/logout')
        else:
            return redirect('/dashboard')
    return redirect('/')

@app.route("/dashboard/<int:order>")
def order_by(order):
    if 'user_id' not in session:
        return redirect('/')
    by = ["title", "network", "release_date"]
    all_shows = Show.get_all_by({'order' : by[order]})
    logged_user = User.get_by_id({'id' : session['user_id']})
    liked_shows_id = Like.get_shows_id_for_user({'id' : session['user_id']})
    user_likes = Like.count_for_user({'user_id' : session['user_id']})
    return render_template("dashboard.html", all_shows = all_shows, user = logged_user, liked_shows_id = liked_shows_id, user_likes=user_likes)



