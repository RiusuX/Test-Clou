import time
import serial
import binascii

#envio y lectura de trama 
def trama(hex_string):
    #Configuracion del puerto
    ser = serial.Serial(port='COM6',baudrate=2400,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_EVEN,
                        stopbits=serial.STOPBITS_ONE)
    #inicia la comunicacion
    ser.isOpen()
    #envio trama de solicitud
    byte_data = bytes.fromhex(hex_string.replace(' ',''))
    print("Trama de datos enviada exitosamente")
    ser.write(byte_data)
    # Lee los datos recibidos desde el puerto serial
    recv=[]
    for i in range(20):  # Inicializar la lista con 20 elementos
        recv.append(binascii.hexlify(ser.read()).decode('utf-8'))
    print("Estos son los datos que llegann",recv)
    ser.close()
    return recv

def cal_two(recv, e):
    a = int(recv[17])-33
    b = int(recv[16])-33
    c = int(recv[15])-33
    d = int(recv[14])-33
    c = str(a)+str(b) #concatenacion de los numeros
    c = int(c)/e
    return c

def cal_two(recv,e):
    a = int(recv[17])-33
    b = int(recv[16])-33
    c = int(recv[15])-33
    d = str(a)+str(b)+str(c) #concatenacion de los numeros
    d = int(d)/ e
    return d

#Potencia activa: '68 16 00 00 00 15 20 68 11 04 33 33 36 35 01 16'
hex_string = '68 16 00 00 00 15 20 68 11 04 33 33 36 35 01 16'
recv = trama(hex_string)
act_power = 
#xx: '68 16 00 00 00 15 20 68 11 04 xx xx xx xx cs 16
#xx: '68 16 00 00 00 15 20 68 11 04 xx xx xx xx cs 16
#xx: '68 16 00 00 00 15 20 68 11 04 xx xx xx xx cs 16
#xx: '68 16 00 00 00 15 20 68 11 04 xx xx xx xx cs 16
#xx: '68 16 00 00 00 15 20 68 11 04 xx xx xx xx cs 16
#xx: '68 16 00 00 00 15 20 68 11 04 xx xx xx xx cs 16



print("Voltaje: ",volt)


