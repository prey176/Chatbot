# main server file for the code
# from try004 import testerstring
import socket
import sys
from threading import *
from backend import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "ip-address"
PORT = 8888
print(HOST)
print(PORT)

try:
	s.bind((HOST,PORT))
except socket.error as err:
	s.close()
	print ('Bind Failed, Error Code: '+ str(err[0])+', Message: '+err[1])
	sys.exit()

class client(Thread):

	def __init__(self,socket,address):
		Thread.__init__(self)
		self.sock = socket
		self.addr = address
		self.start()

	def run(self):
		print ('Connect with ' + self.addr[0]+':'+str(self.addr[1]))

		datarecievd = self.sock.recv(1024).decode()
		print(datarecievd)
		
		r = solveQuery(datarecievd)
		print(r)
		self.sock.send(r.encode())

		print("the data is already send")
		self.sock.close()

threads = []
print ('Socket Bind Success!')

s.listen(10)
print ('Socket Bind Success!')
print('server started and listening')
while True:
	(clientsocket,address) = s.accept()
	client(clientsocket,address).join()