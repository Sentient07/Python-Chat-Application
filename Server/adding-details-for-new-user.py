#!/usr/bin/python
import sys
import threading
import SocketServer
import pickle, hashlib, MySQLdb
host, port = "127.0.0.1", 8887
class MyTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		#print(self.request)

		''' listening to the port on localhost and recieving the data'''
		

		self.data = self.request.recv(1024)
		self.dict = pickle.loads(self.data)
		self.cur_thread = threading.current_thread()
		#print(self.dict)
		print("" + "Thread id is" + str(self.cur_thread))

		user_name = self.dict['user name']
		password = self.dict['passwd']
		fname = self.dict['FirstName']
		sname = self.dict['SecondName']
		email = self.dict['E-mailId']
		#print(user_name)

		e1 = "Details successfully added"
		''' Connecting to the database and saving the details of the User'''
		try :
			db = MySQLdb.connect("localhost","<database-user-name>","<password>","<database name>")
			#print(db)
			c = db.cursor()
			cmd = "INSERT INTO UDETAILS VALUES ('%s', '%s', '%s', '%s', '%s') "
			result = c.execute(cmd, (user_name, password, fname, sname, email))
		except Exception as e :
			self.request.sendto(str(e), self.client_address)
		else :
			self.request.sendto(e1, self.client_address)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	""" Threaded Server Class for asynschronous connection """
	pass
		
def main():
	server = ThreadedTCPServer((host,port), MyTCPHandler)
	server_thread = threading.Thread(target=server.serve_forever)
	server_thread.daemon = True
	server_thread.start()
	print(server.server_address)
	server.serve_forever(poll_interval=0.5)

if __name__ == '__main__':
	main()

