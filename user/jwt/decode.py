import jwt
from graphql_jwt.settings import jwt_settings
from graphql_jwt.utils import get_user_by_payload


def decode_handler(token, context=None):
    payload = jwt.decode(
        token,
        jwt_settings.JWT_SECRET_KEY,
        jwt_settings.JWT_VERIFY,
        options={
            'verify_exp': jwt_settings.JWT_VERIFY_EXPIRATION,
        },
        leeway=jwt_settings.JWT_LEEWAY,
        audience=jwt_settings.JWT_AUDIENCE,
        issuer=jwt_settings.JWT_ISSUER,
        algorithms=[jwt_settings.JWT_ALGORITHM])
    user = get_user_by_payload(payload)
    if user is not None:
        if 'password' not in payload or payload['password'] != user.password[-8:]:
            raise Exception('Password has changed')
    return payload
