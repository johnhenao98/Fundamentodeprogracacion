#Por si las moscas para instalar cosas (pip install 'xx')
# C:\Users\docenteitm\AppData\Local\Programs\Python\Python37\scripts

import requests 
import socket

class PeticionGet:

     def __init__(self, sitio):
         self.sitio = sitio
    
     def pget(self, sitio):

        self.sitio = sitio
        req = requests.get('https://' + self.sitio)
        ip = socket.gethostbyname(self.sitio)
        estatus = req.status_code
        servidor_respuesta = socket.getfqdn(ip)
        print(ip) 
        print(estatus)
        print(req.headers['Server'])
        print (servidor_respuesta)
        print(req.headers['content-type'])
        print("")     
  
sitios = ['www.google.com','www.youtube.com','www.itm.edu.co']

for sitio in sitios:
    p = PeticionGet(sitio)
    p.pget(sitio)