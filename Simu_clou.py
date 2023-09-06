import serial
import binascii
# Configura la conexión serial
ser = serial.Serial(
    port='COM1',  # Elige el puerto serial correcto
    baudrate=2400,  # Configura la velocidad de baudios según tus necesidades
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE
)
#inicia la comunicacion
ser.isOpen()
# Define la trama de solicitud que deseas detectar Potencia activa
Trama_recv = b'\x68\x16\x00\x00\x00\x15\x20\x68\x11\x04\x33\x33\x36\x35\x01\x16'
#activa lectura
#data_hex = []
hex_str = b''
#data = []
for i in range(16):  # Inicializar la lista con n elementos
        #data.append(binascii.hexlify(ser.read()).decode('utf-8'))
        #data_hex.append(binascii.hexlify(ser.read()).decode('utf-8'))
        hex_str=hex_str+ser.read()
#print(data)
print(hex_str)
#comparacion
if hex_str == Trama_recv:
    # Si la trama de solicitud coincide, envía la respuesta
    hex_recv= '68 16 00 00 00 15 20 68 11 04 33 33 36 35 01 16'
    byte_data = bytes.fromhex(hex_recv.replace(' ',''))
    print("Trama de datos enviada exitosamente")
    ser.write(byte_data)
    #for hex in Trama_send:
    #    ser.write(hex)
    print("Respondido a la solicitud")
else:
    # Opcionalmente, puedes manejar otros casos aquí
    print("Solicitud no reconocida")

