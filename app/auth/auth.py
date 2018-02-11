import json
from functools import wraps

from flask import current_app as app, request, jsonify, _request_ctx_stack
from werkzeug.exceptions import HTTPException
from jose import jwt
from six.moves.urllib.request import urlopen

AUTH0_DOMAIN = 'darogina-flask-sample.auth0.com'
API_AUDIENCE = 'https://api.seed.com'
ALGORITHMS = ["RS256"]


# Error handler
class AuthError(HTTPException):
    def __init__(self, description=None, code=None, error_type=None):
        super(AuthError, self).__init__(description=description)
        self.code = code
        self.error_type = error_type


# Format error response and append status code
def get_token_auth_header():
    """Obtains the access token from the Authorization Header
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError(error_type="authorization_header_missing", description="Authorization header is expected", code=401)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError(error_type="invalid_header", description="Authorization header must start with Bearer", code=401)
    elif len(parts) == 1:
        raise AuthError(error_type="invalid_header", description="Token not found", code=401)
    elif len(parts) > 2:
        raise AuthError(error_type="invalid_header", description="Authorization header must be Bearer token", code=401)

    token = parts[1]
    return token


def requires_auth(f):
    """Determines if the access token is valid
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        if app.config.get('FORCE_DISABLE_AUTH'):
            return f(*args, **kwargs)
        token = get_token_auth_header()
        jsonurl = urlopen("https://" + AUTH0_DOMAIN + "/.well-known/jwks.json")
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                    audience=API_AUDIENCE,
                    issuer="https://" + AUTH0_DOMAIN + "/"
                )
            except jwt.ExpiredSignatureError:
                raise AuthError(error_type="token_expired", description="token is expired", code=401)
            except jwt.JWTClaimsError:
                raise AuthError(error_type="invalid_claims", description="incorrect claims, please check the audience and issuer", code=401)
            except Exception:
                raise AuthError(error_type="invalid_header", description="Unable to parse authentication token.", code=400)

            _request_ctx_stack.top.current_user = payload
            return f(*args, **kwargs)
        raise AuthError(error_type="invalid_header", description="Unable to find appropriate key", code=400)

    return decorated


def requires_scope(required_scope):
    """Determines if the required scope is present in the access token
    Args:
        required_scope (str): The scope required to access the resource
    """
    token = get_token_auth_header()
    unverified_claims = jwt.get_unverified_claims(token)
    if unverified_claims.get("scope"):
        token_scopes = unverified_claims["scope"].split()
        for token_scope in token_scopes:
            if token_scope == required_scope:
                return True
    return False
