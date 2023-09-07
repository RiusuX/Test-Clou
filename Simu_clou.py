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
# Define la tramas de solicitud 
Trama_act = b'\x68\x16\x00\x00\x00\x15\x20\x68\x11\x04\x33\x33\x36\x35\x01\x16'
hex_str = b''
for i in range(16):  # Inicializar la lista con n elementos
        hex_str=hex_str+ser.read()
print(hex_str)
#comparacion
if hex_str == Trama_act:
    # Si la trama de solicitud coincide, envía la respuesta
    hex_recv= ["FE" "FE" "68" "31" "00" "00" "00" "15" "20" "68" "91" "07" "33" "33" "36" "35" "7C" "3C" "33" "8A" "16"]
    #byte_data = bytes.fromhex(hex_recv.replace(' ',''))
    print("Trama de datos enviada exitosamente")
    #ser.write(byte_data)
    for i in range(len(hex_recv)):
        a = bytes.fromhex(hex_recv[i])
        ser.write(a)
    print("Respondido a la solicitud")
else:
    # Opcionalmente, puedes manejar otros casos aquí
    print("Solicitud no reconocida")

