import socket
import globals

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clients = []
nicknames = []

def handle(client):
	msg_count = 0
	nickname = None
	clients.append(client)
	
	while True:
		try:
			msg = client.recv()
			

			if msg_count == 0:
				client.send()
			elif msg_count == 1:


			msg_count += 1
			broadcast(msg)
		except Exception as e:
			print(e)
			client.close()
			
			client_index = clients.index(client)
			clients.remove(client_index)

			nickname_index = nicknames.index()
			broadcast(f'')
	
usi
def broadcast(msg):
	for client in clients:
		client.send(f'{msg}'.encode('ascii'))
