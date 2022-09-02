from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime
from rest_framework import status
from apps.users.models import User
from apps.users.serializers import UserRegisterSerializer
from apps.logs.serializers import LogSerializer
from middlewares.log import log
from middlewares.getLocalIp import localIp
from middlewares.currentURL import URL
from middlewares.checkToken import token_validation


# region Index
@api_view(['GET'])
def indexApiView(request):
    return Response({'message': 'Bienvenido'}, status=status.HTTP_200_OK)

# end region


# region Register

@api_view(['POST'])
def registerApiView(request):
    usersSerializer = UserRegisterSerializer(data=request.data)

    if usersSerializer.is_valid():
        usersSerializer.save()
        logsSerializer = LogSerializer(request.data)
        
        # obtener Ip local del usuario
        local_ip = localIp()

        # obtener endpoint que consumio el usuario
        fullURL = URL(request)

        # Guarda en Log los datos cuando un usuario se registra
        jsonData = {
                "users": usersSerializer.data['id'],
                "actionType": 1,
                "ipUser": local_ip,
                "value": "Successfull",
                "url": fullURL
            }
        log(jsonData)

        return Response(usersSerializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(usersSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

# end region

@api_view(['POST'])
def loginApiView(request):
    email = request.data['email']
    password = request.data['password']
    user = User.objects.filter(email=email).first()

    local_ip = localIp()

    fullURL = URL(request)

    if user is None:
        raise AuthenticationFailed('Email incorrecto')

    if user.userType == 1:

        if not user.check_password(password):
            # Guarda en Log los datos cuando un usuario intenta loguearse con contraseña erronea
            jsonData = {
                "users": user.id,
                "actionType": 2,
                "ipUser": local_ip,
                "value": "Unsuccessfull - incorrect password",
                "url": fullURL
            }
            log(jsonData)
            raise AuthenticationFailed('Contraseña incorrecta')

        if user.status == 1:
            payload = {
                'id': user.id,
                'email': user.email,
                'status': user.status,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=43200),
                'iat': datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'Ibrahimovic', algorithm='HS256')

            response = Response()

            response.data = {
                'accessToken':token,
                'idUser':user.id,
                'typeUser':user.userType,
                'statusUser':user.status,
            }

            # Guarda en Log los datos del usuario cuando se loguea exitosamente
            jsonData = {
                "users": user.id,
                "actionType": 2,
                "ipUser": local_ip,
                "value": "Successfull",
                "url": fullURL
            }
            log(jsonData)

            return response

        elif user.status == 2:

            payload = {
                'id': user.id,
                'email': user.email,
                'status': user.status,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=43200),
                'iat': datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'Ibrahimovic', algorithm='HS256')

            response = Response()

            response.data = {
                'accessToken': token,
                'statusUser': user.status
            }

            jsonData = {
                "users": user.id,
                "actionType": 2,
                "ipUser": local_ip,
                "value": "Unsuccessfull - disabled user",
                "url": fullURL
            }
            log(jsonData)

            return response

    else:

        if not user.check_password(password):
            jsonData = {
                "users": user.id,
                "actionType": 2,
                "ipUser": local_ip,
                "value": "Unsuccessfull - incorrect password",
                "url": fullURL
            }
            log(jsonData)
            raise AuthenticationFailed('Contraseña incorrecta')

        if user.status == 1:
            payload = {
                'id': user.id,
                'email': user.email,
                'status': user.status,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=43200),
                'iat': datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'Ibrahimovic', algorithm='HS256')

            response = Response()

            response.data = {
                    'accessToken':token,
                    'idUser':user.id,
                    'typeUser':user.userType,
                    'statusUser':user.status,
                }

            jsonData = {
                "users": user.id,
                "actionType": 2,
                "ipUser": local_ip,
                "value": "Successfull",
                "url": fullURL
            }
            log(jsonData)

            return response

        elif user.status == 2:

            payload = {
            'id':user.id,
            'email':user.email,
            'status':user.status,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=43200),
            'iat':datetime.datetime.utcnow()
            }
        
            token = jwt.encode(payload, 'Ibrahimovic', algorithm='HS256')

            response = Response()

            response.data = {
                'accessToken': token,
                'statusUser': user.status,
            }

            jsonData = {
                "users": user.id,
                "actionType": 2,
                "ipUser": local_ip,
                "value": "Unsuccessfull - disabled user",
                "url": fullURL
            }
            log(jsonData)

            return response

# end region


# region Logout

@api_view(['GET'])
def logoutApiView(request, pk=None):
    token_validation(request,[1,2,3])
    user = User.objects.filter(id=pk).first()

    local_ip = localIp()
    fullURL = URL(request)

    if user:

        jsonData = {
            "users": user.id,
            "actionType": 3,
            "ipUser": local_ip,
            "value": "Successfull",
            "url": fullURL
        }
        log(jsonData)
        return Response({"message": "Sesion cerrada con exito"}, status=status.HTTP_200_OK)

    else:
        return Response({"message": "Usuario inexistente"}, status=status.HTTP_400_BAD_REQUEST)

# end region