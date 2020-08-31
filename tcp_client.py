#import socket library
import socket

#remote details
 remote_host = "google.com"
 remote_port = 80
 
 #create socket object
 
 client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
 #connect to remote host
 
 client.connect(remote_host,remote_port)
 
 #send payloaaaaaf
 
 client.send(b"GET / HTTP/1.1 \r\n Host:google.com \r\n Connection:Keep-Alive \r\n")
 
 #print response
 
 response = client.recv(4096)
 print(response)
