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
Trama_activePower = b'\x68\x16\x00\x00\x00\x15\x20\x68\x11\x04\x33\x33\x36\x35\x01\x16'
Trama_maximumDemand = b'\x68\x16\x00\x00\x00\x15\x20\x68\x11\x04\x33\x33\x34\x34\xFE\x16'
Trama_frequency = b'\x68\x16\x00\x00\x00\x15\x20\x68\x11\x04\x35\x33\xB3\x35\x85\x16'
Trama_totalActiveEnergy = b'\x68\x16\x00\x00\x00\x15\x20\x68\x11\x04\x33\x33\x34\x33\xFD\x16'
Trama_powerFactor = b'\x68\x16\x00\x00\x00\x15\x20\x68\x11\x04\x33\x33\x39\x35\x04\x16'
Trama_voltage = b'\x68\x16\x00\x00\x00\x15\x20\x68\x11\x04\x33\x34\x34\x35\x00\x16'
Trama_curr = b'\x68\x16\x00\x00\x00\x15\x20\x68\x11\x04\x33\x34\x35\x35\x01\x16'

hex_str = b''
for i in range(16):  # Inicializar la lista con n elementos
        hex_str=hex_str+ser.read()

def send_trama(hex_recv):
    for i in range(len(hex_recv)):
        a = bytes.fromhex(hex_recv[i])
        ser.write(a)
     
#comparacion
if hex_str == Trama_activePower:
    #respuesta
    hex_recv= ["FE" "FE" "68" "31" "00" "00" "00" "15" "20" "68" "91" "07" "33" "33" "36" "35" "7C" "3C" "33" "8A" "16"]
    send_trama(hex_recv)
    print("Respondido a la solicitud activePower")
    hex_recv.clear()

if hex_str == Trama_maximumDemand:
    #respuesta
    hex_recv= ["FE" "FE" "68" "31" "00" "00" "00" "15" "20" "68" "91" "0C" "33" "33" "34" "34" "93" "78" "33" "57" "35" "34" "34" "44" "17" "16"]
    send_trama(hex_recv)
    print("Respondido a la solicitud maximumDemand")

if hex_str == Trama_frequency:
    #respuesta
    hex_recv= ["FE" "FE" "68" "31" "00" "00" "00" "15" "20" "68" "91" "06" "35" "33" "B3" "35" "33" "93" "E3" "16"]
    send_trama(hex_recv)
    print("Respondido a la solicitud frequency")

if hex_str == Trama_totalActiveEnergy:
    #respuesta
    hex_recv= ["FE" "FE" "68" "31" "00" "00" "00" "15" "20" "68" "91" "08" "33" "33" "34" "33" "95" "43" "33" "33" "DA" "16"]
    send_trama(hex_recv)
    print("Respondido a la solicitud totalActiveEnergy")

if hex_str == Trama_powerFactor:
    #respuesta
    hex_recv= ["FE" "FE" "68" "31" "00" "00" "00" "15" "20" "68" "91" "06" "33" "33" "39" "35" "33" "3B" "0F" "16"]
    send_trama(hex_recv)
    print("Respondido a la solicitud powerFactor")

if hex_str == Trama_voltage:
    #respuesta
    hex_recv= ["FE" "FE" "68" "31" "00" "00" "00" "15" "20" "68" "91" "06" "33" "34" "34" "35" "57" "45" "39" "16"]
    send_trama(hex_recv)
    print("Respondido a la solicitud voltage")

if hex_str == Trama_curr:
    #respuesta
    hex_recv= ["FE" "FE" "68" "31" "00" "00" "00" "15" "20" "68" "91" "07" "33" "34" "35" "35" "33" "43" "33" "48" "16"]
    send_trama(hex_recv)
    print("Respondido a la solicitud curr")
else:
    # Opcionalmente, puedes manejar otros casos aquí
    print("Solicitud no reconocida")

