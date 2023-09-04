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



print("Trama de datos enviada exitosamente", byte_data)
print(binascii.hexlify(byte_data).decode('utf-8'))

# Lee los datos recibidos desde el puerto serial
ser.write(byte_data)
bytesToRead = ser.inWaiting()
a = ser.read(bytesToRead)
print(binascii.hexlify(a).decode('utf-8'))


ser.close()
