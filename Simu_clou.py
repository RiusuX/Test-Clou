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
Hex_str = b''
#data = []
for i in range(16):  # Inicializar la lista con n elementos
        #data.append(binascii.hexlify(ser.read()).decode('utf-8'))
        #data_hex.append(binascii.hexlify(ser.read()).decode('utf-8'))
        Hex_str=Hex_str+ser.read()
#print(data)
print(Hex_str)
#comparacion
if Hex_str == Trama_recv:
    # Si la trama de solicitud coincide, envía la respuesta
    Trama_send= b'\x68\x16'  # Define tu respuesta
    for hex in Trama_send:
        ser.write(hex)
    print("Respondido a la solicitud")
else:
    # Opcionalmente, puedes manejar otros casos aquí
    print("Solicitud no reconocida")

