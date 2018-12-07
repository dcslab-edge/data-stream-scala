import socket

class Sender:
    def __init__(self,target_ip:str,target_port:int=8000):
        self._ip:str=target_ip
        self._port:int=target_port
        self._socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def connect(self):
        print(self._ip,self._port)
        self._socket.connect((self._ip,self._port))
        print ("TCP Sender connected to "+self._ip+":"+str(self._port))

    def sendData(self,data):
        self._socket.send(data.encode())

    # def sendData(self,data):
    #     try:
    #         print(self._ip,self._port)
    #         self._socket.connect((self._ip,self._port))
    #         print ("TCP Sender connected to "+self._ip+":"+str(self._port))
    #         print(data)
    #         self._socket.send(data.encode())
    #     except Exception as e:
    #             print("something's wrong with %s:%d. Exception is \n%s" % (self._ip, self._port, e))
    #     finally:
    #         self._socket.close()


    #
    # #TCP Client Code:
    # # TCP client example
    #
    # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.connect(("www.hsd.or.kr", 5000))
    # while 1:
    #     data = client_socket.recv(512).decode()
    #     if ( data == 'q' or data == 'Q'):
    #         client_socket.close()
    #         break;
    #     else:
    #         print ("RECEIVED:" , data)
    #         data = input ( "SEND( TYPE q or Q to Quit):" )
    #         if ( data == 'q' or data == 'Q'):
    #             client_socket.send(data.encode())
    #             client_socket.close()
    #             break;
    #         else:
    #             client_socket.send(data.encode())
    # print ("socket colsed... END.")
    #
    #
