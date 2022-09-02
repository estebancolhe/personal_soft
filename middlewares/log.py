from apps.logs.serializers import LogSerializer
from rest_framework.response import Response

def log(jsonData):
    logsSerializer = LogSerializer(data = jsonData)
    if logsSerializer.is_valid():
        logsSerializer.save()
        return Response(logsSerializer.data)
    else:
        return Response(logsSerializer.errors)