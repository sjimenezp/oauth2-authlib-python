from flask import Flask, render_template, url_for, session, redirect
from authlib.integrations.flask_client import OAuth
from config import Config
import json
import os

app = Flask(__name__)

app.config.from_object(Config)

oauth = OAuth(app)
oauth.register(
    name="test_web_app",
    client_kwargs={"scope": "openid profile email"},
    server_metadata_url=f"{app.config['OAUTH2_ISSUER']}/.well-known/openid-configuration",
)


@app.get("/")
def home():
    return render_template(
        "home.html",
        session=session.get("user"),
        pretty=json.dumps(session.get("user"), indent=4),
    )


@app.get("/callback")
def callback():
    token = oauth.test_web_app.authorize_access_token()
    session["user"] = token
    return redirect(url_for("home"))


@app.get("/login")
def login():
    if "user" in session:
        return redirect(url_for("home"))
    return oauth.test_web_app.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )


@app.get("/loggedout")
def loggedout():
    return redirect(url_for("home"))


@app.get("/logout")
def logout():
    id_token = session["user"]["id_token"]
    session.clear()
    return redirect(
        f"{os.getenv('OAUTH2_ISSUER')}/protocol/openid-connect/logout?post_logout_redirect_uri={url_for('loggedout', _external=True)}&id_token_hint={id_token}"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
