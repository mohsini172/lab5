import os
import json
import sys
import datetime
from socket import *


log = open("slog.txt",'wb')
index = dict();



def createIndex(filename,path):
	onlyname =  os.path.splitext(filename)[0];
	onlyname = onlyname.split('-');
	for i in onlyname:

		if i in index:
			index[i].append(path);
		else:
			index[i] = [];
			index[i].append(path);
	# print index;
	# print '-----------------------------------';
	inFile=open(path,'r');
	for line in inFile:
		line = line.split();
		for i in line:
			if i in index:
				index[i].append(path);
			else:
				index[i] = [];
				index[i].append(path);
	return

# createIndex('sample','/home/mohsin/abc/pintos/src/tests/userprog/sample.txt')

def search():
	result = {}
	for root, dirs, files in os.walk("/home"):
		for file in files:
			if file.endswith(".txt"):
				pathname = os.path.join(root, file);
				createIndex(file,pathname);

search();
searchFileName = raw_input("Enter the name of the file");
if searchFileName in index:
	print index[searchFileName];



# serverPort = 49000
# serverSocket = socket(AF_INET,SOCK_STREAM) 
# serverSocket.bind(('0.0.0.0',serverPort)) 
# serverSocket.listen(1)

# print 'The server is ready to receive'

# connectionSocket, addr = serverSocket.accept() 
# sentence = connectionSocket.recv(1024) 


# files = search(sentence,"/home/mohsin/Pictures")

# if len(files)>0:
# 	files = json.dumps(files)
# 	connectionSocket.send(files)
# 	current = datetime.datetime.now()
# 	log.write('Event Type : Recieve\n')
# 	log.write(str(current)+"\n")
# 	log.write("Source IP: " + "127.0.0.1\n")
# 	log.write("Destination IP: "+ str(addr))
# 	log.write("-------------------------------------------\n\n")
# 	sentence = connectionSocket.recv(1024)
# 	reqFile = open(sentence,'rb')
# 	chunk = reqFile.read(1024)
# 	while(chunk):
# 		current = datetime.datetime.now()
# 		connectionSocket.send(chunk)
# 		log.write('Event Type : send\n')
# 		log.write(str(current)+"\n")
# 		log.write("Source IP: " + "127.0.0.1\n")
# 		log.write("Destination IP: "+ str(addr))
# 		log.write("-------------------------------------------\n\n")
# 		chunk = reqFile.read(1024)



# 	print 'Done sending'
# 	connectionSocket.send('Thank you for connecting')
# 	reqFile.close()
# else:
# 	connectionSocket.send("false")

# log.close()
# connectionSocket.close()

