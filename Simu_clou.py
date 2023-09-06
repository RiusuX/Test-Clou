import serial

# Configura la conexión serial
ser = serial.Serial(
    port='COM6',  # Elige el puerto serial correcto
    baudrate=2400,  # Configura la velocidad de baudios según tus necesidades
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE
)

def responder_trama_solicitud():
    # Define la trama de solicitud que deseas detectar
    trama_solicitud = b'68 16 00 00 00 15 20 68 11 04 33 33 36 35 01 16'

    while True:
        # Lee los datos del puerto serial
        data = ser.read(trama_solicitud)
        if data == trama_solicitud:
            # Si la trama de solicitud coincide, envía la respuesta
            respuesta = b'\x68\x16'  # Define tu respuesta
            ser.write(respuesta)
            print("Respondido a la solicitud")
        else:
            # Opcionalmente, puedes manejar otros casos aquí
            print("Solicitud no reconocida")

if __name__ == "__main__":
    try:
        ser.open()
        print("Conexión serial establecida")
        responder_trama_solicitud()
    except Exception as e:
        print(f"Error al comunicarse con el puerto serial: {e}")
    finally:
        ser.close()
