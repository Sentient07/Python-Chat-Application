import sys
import threading
import SocketServer
import pickle, hashlib, MySQLdb
host, port = "127.0.0.1", 8889
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

		#print(user_name)

		''' Connecting to the database and verifying the user name and password'''

		db = MySQLdb.connect("localhost","<database-user-name>","<password>","<database name>")
		#print(db)
		c = db.cursor()
		c.execute(""" SELECT PASSWORD FROM IDENTITY WHERE USER_NAME = %s """ , (user_name,))
		original_pwd = c.fetchone()
		#print(original_pwd[0])

		if original_pwd[0] == password :
			token = "AUTH"
		elif password == "" :
			token = "EMPTY"

		else :
			token = "INVALID"
		#print(token)
		test = self.request.sendto(token, self.client_address)
		


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	"""docstring for ClassName"""
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

