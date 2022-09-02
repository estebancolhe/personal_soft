#obtener endpoint que consumio el usuario
def URL(request):
    path_info = request.META.get('PATH_INFO')
    http_host = request.META.get('HTTP_HOST')
    fullURL = http_host + path_info
    return fullURL