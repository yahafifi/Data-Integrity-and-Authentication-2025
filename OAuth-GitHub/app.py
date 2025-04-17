import os
from flask import Flask, redirect, url_for, session, render_template
from flask_dance.contrib.github import make_github_blueprint, github
from flask_dance.consumer import oauth_error
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

# OAuth blueprint
github_bp = make_github_blueprint(
    client_id=os.getenv("GITHUB_OAUTH_CLIENT_ID"),
    client_secret=os.getenv("GITHUB_OAUTH_CLIENT_SECRET"),
    redirect_url="/",
    scope="read:user"
)
app.register_blueprint(github_bp, url_prefix="/login")

# Handle OAuth errors
@oauth_error.connect_via(github_bp)
def github_oauth_error(blueprint, message, response):
    print("OAuth error:", message)
    session.clear()
    return redirect(url_for("home"))

@app.route("/")
def home():
    if github.authorized:
        return redirect(url_for("profile"))
    return render_template("home.html")

@app.route("/profile")
def profile():
    if not github.authorized:
        return redirect(url_for("home"))

    try:
        resp = github.get("/user")
        if not resp.ok:
            session.clear()
            return redirect(url_for("home"))
        user_info = resp.json()
        return render_template("profile.html", user=user_info)
    except Exception as e:
        print("Error:", e)
        session.clear()
        return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
