'''
  @Title: Cross network chat client built fully in python
  @Author: S.RamanaSubramanyam
  @mail: vxrram95@gmail.com	
  @linkedin 
'''

from __future__ import print_function 
import sys
from PySide.QtCore import *
from PySide.QtGui import *
import socket,pickle, hashlib
#from collections import namedtuple

__IRC__ = " python IRC "





class login1(QDialog):
	"""docstring for login1"""
	def __init__(self, parent=None):
		super(login1, self).__init__(parent)
		

		logo = QPixmap("download.jpg")
		logo_label = QLabel(self)
		logo_label.setPixmap(logo)
		self.namelabel = QLabel(__IRC__)
		idlabel = QLabel("UserName ")
		self.uname = QLineEdit()
		plabel = QLabel("Password ")
		self.pwd = QLineEdit()
		
		host = QLabel("Host Address ")
		self.hostip = QLineEdit()
		port = QLabel("PortNumber ")
		self.portno = QLineEdit()
		self.btn1 = QPushButton("New Member ")
		self.btn2 = QPushButton("Login ")
		self.btn3 = QPushButton("Exit ")
		

		

		layout = QVBoxLayout()
		layout.addWidget(logo_label)
		layout.addWidget(self.namelabel)
		layout.addWidget(idlabel)
		layout.addWidget(self.uname)
		layout.addWidget(plabel)
		layout.addWidget(self.pwd)
		layout.addWidget(host)
		layout.addWidget(self.hostip)
		layout.addWidget(port)
		layout.addWidget(self.portno)
		layout.addWidget(self.btn1)
		layout.addWidget(self.btn2)
		layout.addWidget(self.btn3)
		self.setLayout(layout)


		self.uname.selectAll()
		self.uname.setFocus()

		self.connect(self.btn1, SIGNAL("clicked()"), self.Register)
		self.connect(self.btn2, SIGNAL("clicked()"), self.Checks)
		self.connect(self.btn3, SIGNAL("clicked()"), self.Close)

	def Checks():
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		host = '127.0.0.1'
		port = 8888
		e = "Logged"
		try:
			s.connect((host,port))
			password = hashlib.sha224(self.npwd).hexdigest()
			dict = {'user name': self.newusr, 'passwd': password}
			dumped = pickle.dumps(dict)
			s.sendto(dumped,((host,port)))
			conn, addr = s.accept()
			recieved = s.recv(4096)
		except Exception, e:
			msgbox = QMessageBox()
			msgbox.setText(str(e) + error )
			msgbox.exec_()
			sys.exit()
		finally :
			s.Close()
		if recieved == :
			pass
	def Authenticated():
		mchat = MainWindow()
		mchat.exec_()
	
		
	def Close(self):
		print(str(self.uname.text()))
		test = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		print(test)
		if test == QMessageBox.StandardButton.Yes:
			sys.exit()
		
		
	
	def Register(self):
		new = NewUser()
		new.exec_()

class MainWindow(QDialog):
	"""The main ChatWindow"""
	def __init__(self, parent=None):
		super(ClassName, self).__init__(parent)
		self.Chat = QTextEdit(parent)
		self.chat.setReadOnly(True)
		self.chat.setLineWrapMode(QTextEdit.NoWrap)
		font = self.chat.font()
		font.setFamily("Arial")
		font.setPointSize(10)
		self.chat.moveCursor(QTextCursor.End)
		self.chat.setCurrentFont(font)
		self.chat.setTextColor(black)

		self.chat.insertPlainText(text)

		self.scroll = self.chat.verticalScrollBar()
		self.scroll.setValue(self.scroll.maximum())

		self.messages = QLineEdit()
		
		self.sendbutton = QPushButton("Send")

		self.setWindowTitle("Chat Window ! ")

		self.connect(self.sendbutton, SIGNAL("clicked()"), self.posting_messages)

	def posting_messages():
		pass
			
class HostAlive(object):
	"""To check if the host is alive or not"""
	def __init__(self, arg):
		super(ClassName, self).__init__(parent)
		
		

class NewUser(QDialog):
	"""docstring for NewUser"""
	def __init__(self, parent=None):
		super(NewUser,self).__init__(parent)
		

		nuname = QLabel("UserName ")
		self.newusr = QLineEdit()
		firstname = QLabel("Firstname ")
		self.fname = QLineEdit()
		secondname = QLabel("Secondname ")
		self.nsecondname = QLineEdit()
		emailid = QLabel("E-maid ID ")	
		self.nemail = QLineEdit()
		newpassword = QLabel("Password")
		self.npwd = QLineEdit()
		self.nregbtn = QPushButton("Register")
		self.nrexitbtn = QPushButton("Exit")

		self.setWindowTitle("Register")


		nlayout = QVBoxLayout()
		nlayout.addWidget(nuname)
		nlayout.addWidget(self.newusr)
		nlayout.addWidget(firstname)
		nlayout.addWidget(self.fname)
		nlayout.addWidget(secondname)
		nlayout.addWidget(self.nsecondname)
		nlayout.addWidget(emailid)
		nlayout.addWidget(self.nemail)
		nlayout.addWidget(newpassword)
		nlayout.addWidget(self.npwd)
		nlayout.addWidget(self.nregbtn)
		nlayout.addWidget(self.nrexitbtn)
		self.setLayout(nlayout)

		self.connect(self.nregbtn, SIGNAL("clicked()"), self.passtodb)
		self.connect(self.nrexitbtn, SIGNAL("clicked()"), self.rexit)
	#def passtodb(self):
		
	def rexit(self):
		sys.exit()
	def passtodb(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		host = '127.0.0.1'
		port = 8888
		e = "Details added ! Login again with credentials"
		try:
			s.connect((host,port))
			password = hashlib.sha224(self.npwd).hexdigest()
			dict = {'user name': self.newusr, 'passwd': password, 'FirstName': self.fname, 'SecondName': self.nsecondname, 'E-maid': self.nemail}
			dumped = pickle.dumps(dict)
			s.sendto(dumped,((host,port)))
			conn, addr = s.accept()
			recv = s.recv(4096)
		except Exception, e:
			if str(e) == "[Errno 111] Connection refused":
				error = "The host is dead"
				print(error)
			else :
				print(e)
		msgbox = QMessageBox()
		msgbox.setText(str(e) + error )
		msgbox.exec_()
		sys.exit()

		

def main ():
	app = QApplication(sys.argv)
	display = login1()
	display.show()
	app.exec_()
if __name__ == '__main__':
	main()

