from flask import Flask, redirect, url_for,render_template
from opentok import OpenTok

app = Flask(__name__)

app.config.from_object(__name__)

api_key = "46624262"        # Replace with your OpenTok API key.
api_secret = "9573c22f4f42ff2aff59ffecac728edb7989c156"     # Replace with your OpenTok API secret.

opentok_sdk = OpenTok(api_key, api_secret)

@app.route('/')
def index():
	#session_properties = {OpenTok.SessionProperties.p2p_preference: "disabled"}
	session = opentok_sdk.create_session()#, session_properties)
	url= url_for('chat',session_id=session.session_id)
	return redirect(url)

@app.route('/<session_id>')
def chat(session_id):
 	token=opentok_sdk.generate_token(session_id)
 	return render_template('index.html', api_key=api_key, session_id=session_id, token=token)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
