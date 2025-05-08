from flask import Flask, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = ''  

# Configure OAuth
oauth = OAuth(app)

auth0 = oauth.register(
    'auth0',
    client_id=os.getenv('AUTH0_CLIENT_ID'),
    client_secret=os.getenv('AUTH0_CLIENT_SECRET'),
    client_kwargs={
        'scope': 'openid profile email',
    },
    server_metadata_url=f'https://{os.getenv("AUTH0_DOMAIN")}/.well-known/openid-configuration',
)

@app.route('/')
def home():
    user = session.get('user')
    if user:
        return jsonify(user)
    return '<a href="/login">Login with Auth0</a>'

@app.route('/login')
def login():
    redirect_uri = os.getenv('AUTH0_CALLBACK_URL')
    return auth0.authorize_redirect(redirect_uri=redirect_uri)

# after successful callback
@app.route('/callback')
def callback():
    token = auth0.authorize_access_token()
    id_token = token["userinfo"]          
    print(id_token)
    # Verify that MFA was actually done
    if "mfa" not in id_token.get("amr", []):
        return "MFA was required but not completed", 401

    session["user"] = {
        "name": id_token.get("name"),
        "email": id_token.get("email")
    }
    return redirect("/")


@app.route('/logout')
def logout():
    session.clear()
    return redirect(f'https://{os.getenv("AUTH0_DOMAIN")}/v2/logout?returnTo=http://localhost:5000')

if __name__ == '__main__':
    app.run(debug=True)
