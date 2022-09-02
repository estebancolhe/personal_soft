from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from apps.books.models import Book
from apps.books.serializers import BookSerializer
from middlewares.checkToken import token_validation
from middlewares.log import log
from middlewares.getLocalIp import localIp
from middlewares.currentURL import URL


# region get all books and create book

@api_view(["GET", "POST"])
def allBooksApiView(request):
    token_validation(request,[1,2])


    if request.method == "GET":
        
        idUser=request.headers['idUser']
        
        book = Book.objects.all()

        if book:
            
            booksSerializer = BookSerializer(book, many=True)

            local_ip = localIp()
            fullURL = URL(request)

            jsonData = {
                "users": idUser,
                "actionType": 4,
                "ipUser": local_ip,
                "value": "Successfull",
                "url": fullURL
            }
            log(jsonData)

            return Response(booksSerializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Sin datos"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "POST":

        idUser=request.data['idUser']

        booksSerializer = BookSerializer(data=request.data)
        if booksSerializer.is_valid():
            booksSerializer.save()

            local_ip = localIp()
            fullURL = URL(request)

            jsonData = {
                "users": idUser,
                "actionType": 5,
                "targetId":booksSerializer.data['id'],
                "ipUser": local_ip,
                "value": "Successfull",
                "url": fullURL
            }
            log(jsonData)

            return Response(booksSerializer.data, status=status.HTTP_201_CREATED)
        return Response(booksSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

# end region


# region get specific book and modify book

@api_view(["GET", "PUT"])
def specificBookApiView(request, pk=None,idUser=None):
    token_validation(request,[1,2])

    book = Book.objects.filter(id=pk).first()

    if book:

        if request.method == "GET":

            booksSerializer = BookSerializer(book)

            local_ip = localIp()
            fullURL = URL(request)

            jsonData = {
                "users": idUser,
                "actionType": 6,
                "targetId": booksSerializer.data['id'],
                "ipUser": local_ip,
                "value": "Successfull",
                "url": fullURL
            }
            log(jsonData)

            return Response(booksSerializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':

            booksSerializer = BookSerializer(book, data=request.data)
            if booksSerializer.is_valid():
                booksSerializer.save()

                local_ip = localIp()
                fullURL = URL(request)

                jsonData = {
                    "users": idUser,
                    "actionType": 7,
                    "targetId":book.id,
                    "ipUser": local_ip,
                    "value": "Successfull",
                    "url": fullURL
                }
                log(jsonData)

                return Response(booksSerializer.data, status=status.HTTP_200_OK)
            return Response(booksSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
            return Response({"message": "Datos no encontrados"}, status=status.HTTP_400_BAD_REQUEST)

# end region


# region delete specific book

@api_view(["DELETE"])
def deleteBookApiView(request, pk=None,idUser=None):
    token_validation(request,[2])

    book = Book.objects.filter(id=pk).first()
    
    if book:

        local_ip = localIp()
        fullURL = URL(request)

        jsonData = {
            "users": idUser,
            "actionType": 10,
            "targetId":book.id,
            "ipUser": local_ip,
            "value": "Successfull",
            "url": fullURL
        }
        log(jsonData)

        book.delete()

        return Response({'message':'Libro eliminado correctamente!'},status = status.HTTP_200_OK)
    else:
        return Response({'message':'Datos no encontrados'},status = status.HTTP_400_BAD_REQUEST)

# end region