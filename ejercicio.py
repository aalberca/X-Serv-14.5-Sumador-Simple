#este ejercicio suma los numeros que se le pasan por el GET, de dos en dos.
import socket


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

mySocket.bind(('suma.edu', 8080))

mySocket.listen(5)

print mySocket
primero = 0
try:
	while True:
		print 'Waiting for connections'
		(recvSocket, address) = mySocket.accept()
		print 'Requiest received:'
		peticion = recvSocket.recv(1301)
		print peticion
		try:
			entero = int(peticion.split()[1][1:])
		except ValueError:
			print 'ASDOFIAJSDFOAIJFA'
			continue
		print entero
		print 'Answering back...'
		
		if (primero == 0):
			primero = entero
			print recvSocket.send("HTTP/1.1 200 ok\r\n\r\n" + 
							   "<html><body>" + 
							   '<p>Me has mandado ' + str(entero) + ' Dame otro numero</p>'
							   "</body><html>" + "\r\n")
		else:
			suma = entero + primero
			print recvSocket.send("HTTP/1.1 200 ok\r\n\r\n" + 
							   	"<html><body>" + 
							   	'<p>Me has mandado ' + str(entero) + '</p>'
							   	'<p>' + str(primero) + '+' + str(entero) + '=' + str(suma) + '</p>'
							   	"</body><html>" + "\r\n")
			primero = 0
		recvSocket.close()
		
except KeyboardInterrupt:
	print "Closing binded socket"
	mySocket.close()