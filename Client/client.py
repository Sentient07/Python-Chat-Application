#!/usr/bin/python

'''

  @Title: Cross network chat client built fully in python
  @Author: S.RamanaSubramanyam
  @mail: vxrram95@gmail.com	
  @linkedin: https://in.linkedin.com/in/ramanasubramanyam
  @Github: https://www.github.com/Sentient07

'''

from __future__ import print_function 
import sys
from PySide.QtCore import *
from PySide.QtGui import *
import socket,pickle, hashlib

__IRC__ = " Python Chat Client Application "


class login1(QDialog):
	"""docstring for login1"""
	def __init__(self, parent=None):
		super(login1, self).__init__(parent)
		
		logo = QPixmap("download.jpg")
		logo_label = QLabel(self)
		logo_label.setPixmap(logo)
		self.namelabel = QLabel(__IRC__)
		fontsize = self.namelabel.font()
		fontsize.setPointSize(24)
		
		idlabel = QLabel("UserName ")
		self.uname = QLineEdit()
		self.uname.setMaxLength(10)
		
		plabel = QLabel("Password ")
		self.pwd = QLineEdit()
		self.pwd.setEchoMode(QLineEdit.Password)
		
		host = QLabel("Host Address ")
		self.hostip = QLineEdit()
		
		port = QLabel("PortNumber ")
		self.portno = QLineEdit()
		
		self.btn1 = QPushButton("New Member ")
		self.btn2 = QPushButton("Login ")
		self.btn3 = QPushButton("Exit ")
		

		layout = QVBoxLayout()
		layout.addWidget(self.namelabel)
		layout.addWidget(logo_label)
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

		self.setWindowTitle("Welcome !")


		self.uname.selectAll()
		self.uname.setFocus()

		self.connect(self.btn1, SIGNAL("clicked()"), self.Register)
		self.connect(self.btn2, SIGNAL("clicked()"), self.Checks)
		self.connect(self.btn3, SIGNAL("clicked()"), self.Close)

	

	def Checks(self):
	

		""" Verifies the UserName and password combinations """


		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		host = self.hostip.text()
		try:
			port = int(self.portno.text())
			
		except Exception, e1:
			msgbox = QMessageBox()
			msgbox.setText(str(e1))
			msgbox.exec_()
		
		e = "Logged"

		try:
			sock.connect((host,port))
			password = hashlib.sha224(self.npwd.text()).hexdigest()
			dict = {'user name': self.newusr.text(), 'passwd': password}
			dumped = pickle.dumps(dict)
			sock.sendto(dumped,((host,port)))
			conn, addr = sock.accept()
			recieved = sock.recv(4096)

		except Exception, e:
			msgbox = QMessageBox()
			msgbox.setText("Authenticatication error")
			msgbox.exec_()
			#sys.exit()
		
		finally :
			sock.close()

		try :
			if recieved == "EMPTY" or recieved == "INVALID":
				msgbox = QMessageBox()
				msgbox.setText("Authentication Failure")
				msgbox.exec_()
				sys.exit()

			else :
				mchat = MainWindow()
				mchat.exec_()
				closeEvent(event)
		except Exception, f:
			msgbox = QMessageBox()
			msgbox.setText(str(f))
			msgbox.exec_()

	
		
	def Close(self):
			
		""" Code for Exit Button """

		test = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if test == QMessageBox.StandardButton.Yes:
			sys.exit()
		
		
	
	def Register(self):

		new = NewUser()
		new.exec_()
		closeEvent(event)

	def closeEvent(self, event):

		event.accept()
		


class MainWindow(QDialog):


	"""The Main Chat Window"""


	def __init__(self, parent=None):


		super(MainWindow, self).__init__(parent)
		self.chat = QTextEdit(parent)
		self.chat.setReadOnly(True)
		self.chat.setLineWrapMode(QTextEdit.NoWrap)
		font = self.chat.font()
		font.setFamily("Arial")
		font.setPointSize(10)
		self.chat.moveCursor(QTextCursor.End)
		self.chat.setCurrentFont(font)
		self.chat.setTextColor('black')

		#self.chat.insertPlainText(text)

		self.scroll = self.chat.verticalScrollBar()
		self.scroll.setValue(self.scroll.maximum())

		self.messages = QLineEdit()
		
		self.sendbutton = QPushButton("Send")

		self.setWindowTitle("Chat Window ! ")

		layout = QVBoxLayout()
		layout.addWidget(self.chat)
		layout.addWidget(self.scroll)
		layout.addWidget(self.messages)
		layout.addWidget(self.sendbutton)
		self.setLayout(layout)

		layout.resize(500,400)

		self.connect(self.sendbutton, SIGNAL("clicked()"), self.posting_messages)

	def closeEvent(self, event):

		event.accept()


	def posting_messages(self):

		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		host = self.hostip.text()
		port = 8889
		
		try:
			sock.connect((host,port))
		
		except Exception, e2:
			msgbox = QMessageBox()
			msgbox.setText(str(e2))
			msgbox.exec_()
			#sys.exit()
		else :
		message = self.messages.text()
		sock.sendto(message,((host,port)))	
			while True:
				recieved = sock.recv(4096)
				self.chat.insertPlainText(recieved)
				self.messages.setText("")
		



class NewUser(QDialog):
		

	""" Registers the new user to the Chat """


	def __init__(self, parent=None):
	

		super(NewUser,self).__init__(parent)
	
		nuname = QLabel("User Name ")
		self.newusr = QLineEdit()
		self.newusr.setMaxLength(10)
		firstname = QLabel("Firstname ")
		self.fname = QLineEdit()
		self.fname.setMaxLength(10)
		secondname = QLabel("Secondname ")
		self.nsecondname = QLineEdit()
		self.nsecondname.setMaxLength(10)
		emailid = QLabel("E-maid ID ")	
		self.nemail = QLineEdit()
		newpassword = QLabel("Password")
		self.npwd = QLineEdit()
		self.npwd.setEchoMode(QLineEdit.Password)
		newpasswordrepeat = QLabel("Re-Enter Your Password ")
		self.npwdr = QLineEdit()
		self.npwdr.setEchoMode(QLineEdit.Password)
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
		nlayout.addWidget(newpasswordrepeat)
		nlayout.addWidget(self.npwdr)
		nlayout.addWidget(self.nregbtn)
		nlayout.addWidget(self.nrexitbtn)
		self.setLayout(nlayout)

		self.connect(self.nregbtn, SIGNAL("clicked()"), self.passtodb)
		self.connect(self.nrexitbtn, SIGNAL("clicked()"), self.rexit)
		

	def rexit(self):

		sys.exit()


	def passtodb(self):

			
		""" Passes the user details to the database """


		if self.newusr.text() == "" or self.fname.text() == "" or self.nsecondname.text() == "" or self.nemail.text() == "" or self.npwd.text() == "" :

			msgbox = QMessageBox()
			msgbox.setText("Fill in the details properly ! ")
			msgbox.exec_()
		elif self.npwd.text() != self.npwdr.text() :

			msgbox = QMessageBox()
			msgbox.setText("Passwords do not match ! Enter again")
			msgbox.exec_()
		else :
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			host = '127.0.0.1'
			port = 8887
			e = "Details added ! Login again with credentials"

			try:
				s.connect((host,port))
				password = hashlib.sha224(self.npwd.text()).hexdigest()
				dict = {'user name': self.newusr.text(), 'passwd': password, 'FirstName': self.fname.text(), 'SecondName': self.nsecondname.text(), 'E-maid': self.nemail.text()}
				dumped = pickle.dumps(dict)
				s.sendto(dumped,((host,port)))
				conn, addr = s.accept()
				recv = s.recv(1024)
		
			except Exception, e:
				msgbox = QMessageBox()
				msgbox.setText(str(e))
				msgbox.exec_()
				sys.exit()

			msgbox = QMessageBox()
			msgbox.setText(str(recv))
			msgbox.exec_()
		

def main ():

	app = QApplication(sys.argv)
	display = login1()
	display.show()
	app.exec_()


if __name__ == '__main__':
	main()
