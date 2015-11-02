import socket, ssl, pprint
import binascii
import sys

SERVER = sys.argv[1]
PORT = sys.argv[2]


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = ssl.wrap_socket(s, ca_certs="/tmp/server.crt",certfile="/tmp/client-cert.pem",keyfile="/tmp/client-privkey.pem")
ssl_sock.connect((SERVER, int(PORT)))
print repr(ssl_sock.getpeername())
print ssl_sock.cipher()
print pprint.pformat(ssl_sock.getpeercert())
byte_array='\x05\x01\x00'
while 1:
    ssl_sock.write(byte_array)
    print "Sending: %s" %byte_array.encode('hex')
    data = ssl_sock.read()
    print "Printing: %s"%data
    print "length: %s"%len(data)
    print 'received "%s"' % binascii.hexlify(data)
    print 'As hex %s'%data.encode('hex')

    ssl_sock.write(byte_array)
    if len(data) < 1:
        break
s.close()
