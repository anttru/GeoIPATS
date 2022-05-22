from time import sleep, time
import socket
from iplocator.utils import unique_identifier, create_packet


class TimeoutException(Exception):
    pass

def traceroute(ip, maxhops = 30):
        #Implementación de traceroute, haciendo uso de la funcion ttlicmpecho(), retorna una lista de ips
        routers = []
        for ttl in range(1,maxhops+1):
            router = None
            router = ttlicmpecho(ip, ttl = ttl)
            if router:
                routers.append(router)
            if router == ip:
                break
        return routers
    
def ttlicmpecho(ip, count = 3, interval = 0.5, timeout = 0.6, ttl = 30):
    #Esta función manda peticiones de echo individuales con un ttl dado, buscando que responda un hop intermedio, la usare para implementar mi propio traceroute
    icmpsocket =  socket.socket(family=socket.AF_INET, type=socket.SOCK_RAW,proto=socket.IPPROTO_ICMP)
    #Se crea una socket raw, que administramos desde la programación en vez del kernel
    replies = []
    id = unique_identifier() #se crea el idenfiticador
    reply = None
    for sequence in range(count):
        sleep(interval) # Para no enviar todas las peticiones de golpe esperamos medio segundo entre paquetes
        try:
            send(ip,id, sequence, icmpsocket, ttl)
            reply = None
            reply = receive(timeout, icmpsocket) #receive retornará directamente la ip del router que responde
            
        except Exception as e:
            pass

        replies.append(reply)
    #Hemos hecho varios intentos, miramos si alguno ha respondido y si lo ha hecho, retornamos esa ip como resultado
    for reply in replies:
        if reply:
            return reply

def send(ip, id, sequence, icmpsocket : socket.socket, ttl):
    #esta función envía desde una socket con un tll, ip objetivo e id especificadas como argumentos
    packet = create_packet(id, sequence) #montamos el paquete a envíar
    icmpsocket.setsockopt(socket.IPPROTO_IP, socket.IP_TTL,ttl) #Se configura el ttl en la socket
    target = socket.getaddrinfo(ip, port=None, family= icmpsocket.family, type=icmpsocket.type)[0][4] #Se obtiene el objetivo en formato necesario para la socket
    icmpsocket.sendto(packet, target)

def receive(timeout, icmpsocket : socket.socket):
    #esta funcion recibe en una socket dada con un timeout dado
    icmpsocket.settimeout(timeout)
    time_limit = time() + timeout #calculo del tiempo límite para recibir respuesta
    try:
        while True:
            response = icmpsocket.recvfrom(1024)
            current_time = time()
            source = None
            source = response[1][0] #Se obtiene el remitente de la respuesta obtenida

            if current_time > time_limit:
                raise socket.timeout
            return source
    
    except socket.timeout:
        raise TimeoutException("Tiempo de espera superado ({}s)".format(timeout))
    except OSError:
        raise OSError