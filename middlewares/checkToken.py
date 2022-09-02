from rest_framework.exceptions import AuthenticationFailed
import jwt
from apps.users.models import User

# autenticacion personalizada

def token_validation(request, list):

    tokenFront = request.headers['token']

    if not tokenFront:
        raise AuthenticationFailed('Sin autenticar')
    aux=False
    try:
        user = User.objects.filter(id=jwt.decode(tokenFront, 'Ibrahimovic', algorithms=['HS256'])['id'])
        if user.values()[0]['status'] != 2:
            for i in range(len(list)):
                if list[i] == user.values()[0]['userType']:
                    aux=True
                    break
                else:
                    aux=False
        else:
            raise AuthenticationFailed('Usuario no habilitado')
            
        if aux==True:
            payload=jwt.decode(tokenFront, 'Ibrahimovic', algorithms=['HS256'])
        else:
            raise AuthenticationFailed('Sin permisos')

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token expiró')