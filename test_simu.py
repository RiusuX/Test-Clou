import binascii

hex_string = '68 16 00 00 00 15 20 68 11 04 35 33 B3 35 85 16'
byte_data = bytes.fromhex(hex_string.replace(' ','')) 
Trama_recv = b'\x68\x16\x00\x00\x00\x15\x20\x68\x11\x04\x35\x33\xB3\x35\x85\x16'
if Trama_recv==byte_data:
    print("solicitud recibida")
    #Trama_send = [b'\x68' b'\x16' b'\x00' b'\x00' b'\x00' b'\x15' b'\x20' b'\x68' b'\x11' b'\x04' b'\x35' b'\x33' b'\xB3' b'\x35' b'\x85' b'\x16']
    Trama_send = b'\x68\x16\x00\x00\x00\x15\x20\x68\x11\x04\x35\x33\xB3\x35\x85\x16'
    #print(binascii.hexlify(trama_hex_con_saltos).decode('utf-8'))
    for byte in Trama_send:
        print(hex(byte))
else:
    print("no esta bien perro hp")