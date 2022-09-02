from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from apps.logs.models import ActionType
from apps.logs.serializers import ActionTypeSerializer
from middlewares.checkToken import token_validation
from middlewares.log import log
from middlewares.getLocalIp import localIp
from middlewares.currentURL import URL


# region get all action type and create action type

@api_view(["GET", "POST"])
def allActionTypeApiView(request):
    token_validation(request,[2])

    if request.method == "GET":

        idUser=request.headers['idUser']
        
        actionType = ActionType.objects.all()

        if actionType:
            
            actionTypesSerializer = ActionTypeSerializer(actionType, many=True)

            local_ip = localIp()
            fullURL = URL(request)

            jsonData = {
                "users": idUser,
                "actionType": 8,
                "ipUser": local_ip,
                "value": "Successfull",
                "url": fullURL
            }
            log(jsonData)

            return Response(actionTypesSerializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Sin datos"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "POST":

        idUser=request.data['idUser']

        actionTypesSerializer = ActionTypeSerializer(data=request.data)
        if actionTypesSerializer.is_valid():
            actionTypesSerializer.save()

            local_ip = localIp()
            fullURL = URL(request)

            jsonData = {
                "users": idUser,
                "actionType": 9,
                "targetId":actionTypesSerializer.data['id'],
                "ipUser": local_ip,
                "value": "Successfull",
                "url": fullURL
            }
            log(jsonData)

            return Response(actionTypesSerializer.data, status=status.HTTP_201_CREATED)
        return Response(actionTypesSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

# endregion


# region get specific action type and modify action type

@api_view(["GET", "PUT"])
def specificActiontypeApiView(request, pk=None,idUser=None):
    token_validation(request,[2])

    actionType = ActionType.objects.filter(id=pk).first()

    if actionType:

        if request.method == "GET":

            actionTypesSerializer = ActionTypeSerializer(actionType)

            local_ip = localIp()
            fullURL = URL(request)

            jsonData = {
                "users": idUser,
                "actionType": 11,
                "targetId": actionTypesSerializer.data['id'],
                "ipUser": local_ip,
                "value": "Successfull",
                "url": fullURL
            }
            log(jsonData)

            return Response(actionTypesSerializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':

            actionTypesSerializer = ActionTypeSerializer(actionType, data=request.data)
            if actionTypesSerializer.is_valid():
                actionTypesSerializer.save()

                local_ip = localIp()
                fullURL = URL(request)

                jsonData = {
                    "users": idUser,
                    "actionType": 12,
                    "targetId":actionType.id,
                    "ipUser": local_ip,
                    "value": "Successfull",
                    "url": fullURL
                }
                log(jsonData)

                return Response(actionTypesSerializer.data, status=status.HTTP_200_OK)
            return Response(actionTypesSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
            return Response({"message": "Datos no encontrados"}, status=status.HTTP_400_BAD_REQUEST)

# end region


# region delete action type

@api_view(["DELETE"])
def deleteActionTypeApiView(request, pk=None,idUser=None):
    token_validation(request,[2])

    actionType = ActionType.objects.filter(id=pk).first()

    if actionType:

        local_ip = localIp()
        fullURL = URL(request)

        jsonData = {
            "users": idUser,
            "actionType": 13,
            "targetId":actionType.id,
            "ipUser": local_ip,
            "value": "Successfull",
            "url": fullURL
        }
        log(jsonData)
        
        actionType.delete()

        return Response({'message':'Tipo de accion eliminada correctamente!'},status = status.HTTP_200_OK)
    else:
        return Response({'message':'Datos no encontrados'},status = status.HTTP_400_BAD_REQUEST)

# end region