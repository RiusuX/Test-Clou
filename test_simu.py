import binascii
hex_string = '68 16 00 00 00 15 20 68 11 04 35 33 B3 35 85 16'
byte_data = bytes.fromhex(hex_string.replace(' ','')) 
Trama_recv = b'\x68\x16\x00\x00\x00\x15\x20\x68\x11\x04\x35\x33\xB3\x35\x85\x16'
if Trama_recv==byte_data:
    print("solicitud recibida")
    Trama_send = b'\x68\x16\x00\x00\x00\x15\x20\x68\x11\x04\x35\x33\xB3\x35\x85\x16'
    for byte in Trama_send:
        print(hex(byte))
else:
    print("no esta bien perro hp")