from functools import wraps
from flask import request, Response, redirect, Flask
from bokeh.util import token

app = Flask(__name__)

def check_auth(username, password):
    return username == 'jcarbone' and password == 'password'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/')
@requires_auth
def redirect_to_bokeh():
    s_id = token.generate_secret_key()
    return redirect("http://localhost:5006/iris_kmeans/?bokeh-session-id={}".format(s_id), code=302)

if __name__ == "__main__":
    app.run()
