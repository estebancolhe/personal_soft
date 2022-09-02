import socket
#obtener Ip local del usuario
def localIp():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip