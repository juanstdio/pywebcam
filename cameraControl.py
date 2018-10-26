import urllib.request
#POR FAVOR SETEA ESTO!!
user = 'YourwebCamUsername'
paswd = 'yourWebCamPass'
ip = '192.168.2.122'
typo_call= '/decoder_control.cgi'

#FIJATE QUE ESTO COINCIDA CON TU CAMARA, DE LO CONTRARIO NO FUNCIONARA

typo_stream = '/videostream.cgi'
#fin POR FAVOR SETEA ESTO!!

#No te olvides de cambiar los ajustes de tu camara, no todas trabajan de la misma forma ni tienen los mismos "llamados"
#al final de cada comando
#Arriba = 0
#Abajo = 2
#Izquierda = 4
#Derecha = 6
#Patrol Horizontal = 28
#Patrol Vertical = 26


base_url ='http://'+ip+typo_call
base_url_stream = 'http://'+ip+typo_stream

def stream():
    return (base_url_stream+'?user='+user+'&pwd='+paswd)
def arriba():
    urllib.request.urlopen(base_url+'?user='+user+'&pwd='+paswd+'&command'+str(0))

def abajo():
    urllib.request.urlopen(base_url+'?user='+user+'&pwd='+paswd+'&command'+str(2))

def izquierda():
    urllib.request.urlopen(base_url+'?user='+user+'&pwd='+paswd+'&command'+str(4))

def derecha():
    urllib.request.urlopen(base_url+'?user='+user+'&pwd='+paswd+'&command'+str(6))

def patrol_y():
    urllib.request.urlopen(base_url+'?user='+user+'&pwd='+paswd+'&command'+str(26))

def patrol_x():
    urllib.request.urlopen(base_url+'?user='+user+'&pwd='+paswd+'&command'+str(28))

def stopAll():
    urllib.request.urlopen(base_url+'?user='+user+'&pwd='+paswd+'&command'+str(1))
    urllib.request.urlopen(base_url+'?user='+user+'&pwd='+paswd+'&command'+str(29))
    urllib.request.urlopen(base_url+'?user='+user+'&pwd='+paswd+'&command'+str(27))
