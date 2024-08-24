from config import CLIENT_SECRET, OAUTH_URL, REDIRECT_URI, BOT_TOKEN
from flask import Flask, render_template, request, session, redirect, jsonify
from utils import get_token, get_user_guilds, get_current_user, get_user_connections

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the_secret_keyy'

@app.route("/")
def home():
    if 'token' not in session:
        return redirect(OAUTH_URL)
    return render_template("index.html", current_user=get_current_user)

@app.route("/oauth/callback")
def callback():
    token = get_token(request.args.get('code'))
    session['token'] = token
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if 'token' not in session:
        return redirect(OAUTH_URL)
    current_user = get_current_user(session.get('token'))
    user_guilds = get_user_guilds(session.get('token'))
    user_connections = get_user_connections(session.get('token'))
    
    with open(f'account.txt', 'w') as file:
        file.write(format(current_user))
        file.write(format(user_guilds))
        file.write(format(user_connections))
    #return render_template('dashboard.html', current_user=current_user, user_guilds=user_guilds, 
                           #user_connections=user_connections)
    return redirect("https://discord.com/channels/@me")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
