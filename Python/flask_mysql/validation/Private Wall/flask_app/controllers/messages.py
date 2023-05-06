from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.message import Message


@app.route('/messages/create', methods = ['POST'])
def create_message():
    if Message.validate(request.form['message']):
        if request.form['receiver_id'] == "All":
            all = User.get_except({'id':session['user_id']})
            for receiver in all :
                # print("*"*30, receiver, '#'*30)
                data = {
                    **request.form, 
                    'sender_id' : session['user_id'],
                    'receiver_id' : receiver.id
                }
                Message.create(data)
        else :
            data = {
                **request.form ,'sender_id' : session['user_id']
            }
            Message.create(data)
    return redirect('/dashboard')

@app.route('/messages/<int:message_id>/delete')
def delete(message_id):
    #GETTING LOGGED IN USER ALL MESSAGES
    messages = Message.get_messages_for_receiver({'id' : session['user_id']})
    for message in messages :
        if message.id == message_id:
            Message.delete({'id' : message_id})
            return redirect('/dashboard')
    User.add_warning({'id' : session['user_id']})
    hacker = User.get_by_id({'id' : session['user_id']})
    # print('!'*30, hacker, '!'*30)
    if hacker.warning < 2 :
        ip_address = request.remote_addr
        return render_template('danger.html', hacker = hacker, message_id = message_id, ip_address=ip_address)
    return redirect ('/logout')