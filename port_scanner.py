import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = input("Enter Target IP Address: ")

def scanner(port):
        try:
                sock.connect((target,port))
                return True
        except:
                return False
for portNum in range(1,100):
        print("Scanning port: ", portNum)
        if scanner(portNum):
                print('[*] Port', portNum, '/tcp','is open')
