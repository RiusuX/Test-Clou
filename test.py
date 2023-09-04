import time
import serial
import binascii

ser = serial.Serial(
    port='COM6',
    baudrate=2400,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE
)
ser.isOpen()
#VOLTA: 68 16 00 00 00 15 20 68 11 04 33 34 34 35 1B 16
hex_string = '68 16 00 00 00 15 20 68 11 04 33 34 34 35 00 16'
byte_data = bytes.fromhex(hex_string.replace(' ',''))
datos = []

#Envio de trama
print("Trama de datos enviada exitosamente", byte_data)
print(binascii.hexlify(byte_data).decode('utf-8'))
ser.write(byte_data)


# Lee los datos recibidos desde el puerto serial
recv=[]
for i in range(20):  # Inicializar la lista con 20 elementos
    recv.append(binascii.hexlify(ser.read()).decode('utf-8'))
    #print("dato # ", i + 1, ":", recv[i])

print("Estos son los datos que llegann",recv)

#payload
a = int(recv[17])-33
b = int(recv[16])-33
volt = str(a)+str(b)
volt= int(volt)/10
print("Voltaje: ",volt)

ser.close()
