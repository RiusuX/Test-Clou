import serial
import binascii
import json

#Configuracion del puerto
ser = serial.Serial(port='COM2',baudrate=2400,
                    bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_EVEN,
                    stopbits=serial.STOPBITS_ONE)
#inicia la comunicacion
ser.isOpen()

#envio y lectura de trama 
def trama(hex_string,tam):
    #envio trama de solicitud
    byte_data = bytes.fromhex(hex_string.replace(' ',''))
    #print("Trama de datos enviada exitosamente")
    ser.write(byte_data)
    # Lee los datos recibidos desde el puerto serial
    recv=[]
    for i in range(tam):  # Inicializar la lista con n elementos
        recv.append(binascii.hexlify(ser.read()).decode('utf-8'))
    #print("Estos son los datos que llegann",recv)
    return recv
def str_cero(a):
    if a == "0":
        a = str(a)+str(0)
    else:
        a= str(a)
    return a

def cal(recv,dat,base):
    tam = len(recv)
    a = hex(int(recv[tam-3], 16)-51)[2:] 
    b = hex(int(recv[tam-4], 16)-51)[2:]
    c = hex(int(recv[tam-5], 16)-51)[2:]
    d = hex(int(recv[tam-6], 16)-51)[2:]
    if dat == 2:
        val = str_cero(a)+str_cero(b)
        val = int(val)/ base
    elif dat == 3:
        val = str_cero(a)+str_cero(b)+str_cero(c)
        val = int(val)/ base
    elif dat == 4:
        val = str_cero(a)+str_cero(b)+str_cero(c)+str_cero(d)
        val = int(val)/ base
    else:
        a = hex(int(recv[tam-8], 16)-51)[2:]
        b = hex(int(recv[tam-9], 16)-51)[2:]
        c = hex(int(recv[tam-10], 16)-51)[2:]
        val = str_cero(a)+str_cero(b)+str_cero(c)
        val = int(val)/ base
    return val

#Potencia activa: '68 16 00 00 00 15 20 68 11 04 33 33 36 35 01 16'
hex_string = '68 16 00 00 00 15 20 68 11 04 33 33 36 35 01 16'
recv = trama(hex_string,21)
activePower=cal(recv,3,10000)
#print("La potencia activa es de : ",activePower)

#Maxima demanda: '68 16 00 00 00 15 20 68 11 04 33 33 34 34 FE 16'
hex_string = '68 16 00 00 00 15 20 68 11 04 33 33 34 34 FE 16'
recv = trama(hex_string,26)
maximumDemand=cal(recv,8,10000)
#print("La maxima demanda es de : ",maximumDemand)

#Frecuencia: '68 16 00 00 00 15 20 68 11 04 35 33 B3 35 85 16'
hex_string = '68 16 00 00 00 15 20 68 11 04 35 33 B3 35 85 16'
recv = trama(hex_string,20)
frequency=cal(recv,2,100)
#print("La frecuencia es de : ",frequency)

#Total energia: '68 16 00 00 00 15 20 68 11 04 33 33 34 33 FD 16'
hex_string = '68 16 00 00 00 15 20 68 11 04 33 33 34 33 FD 16'
recv = trama(hex_string,22)
totalActiveEnergy=cal(recv,4,100)
#print("La potencia activa es de : ",totalActiveEnergy)

#Factor de potencia: '68 16 00 00 00 15 20 68 11 04 33 33 39 35 04 16'
hex_string = '68 16 00 00 00 15 20 68 11 04 33 33 39 35 04 16'
recv = trama(hex_string,20)
powerFactor=cal(recv,2,1000)
#print("El factor de potencia es de : ",powerFactor)

#voltaje: '68 16 00 00 00 15 20 68 11 04 33 34 34 35 00 16'
hex_string = '68 16 00 00 00 15 20 68 11 04 33 34 34 35 00 16'
recv = trama(hex_string,20)
voltage=cal(recv,2,10)
#print("El voltaje es de : ",voltage)

#correinte: '68 16 00 00 00 15 20 68 11 04 33 34 35 35 01 16'
hex_string = '68 16 00 00 00 15 20 68 11 04 33 34 35 35 01 16'
recv = trama(hex_string,21)
curr=cal(recv,3,1000)
#print("La corriente es de : ",curr)

#Json create
x = {
  "activePower": activePower,
  "maximumDemand": maximumDemand,
  "frequency": frequency,
  "totalActiveEnergy": totalActiveEnergy,
  "powerFactor": powerFactor,
  "voltage": voltage,
  "curr": curr
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y) 


