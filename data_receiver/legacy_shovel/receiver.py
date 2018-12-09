import socket
import argparse

class Receiver:
    def __init__(self,target_ip:str,target_port:int):
        self._ip:str=target_ip
        self._port:int=target_port
        self._socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def receive(self,backlog:int):
        try:
            self._socket.connect((self._ip,self._port))
            while 1:
                rec=conn.recv(65536).decode()
                if rec!='':
                    print(rec)
            
        except Exception as e:
            print("something's wrong with %s:%d. Exception is %s" % (self._ip, self._port, e))
        finally:
            self._socket.close()

def main():
    parser = argparse.ArgumentParser(description='data receiver')
    #parser.add_argument('-s','--save',action=saveable_dir,help='save data in specified path')

    rec:Receiver = Receiver("localhost",8888)


if __name__=="__main__" :
    main()
#
#
#
# while 1:
#         client_socket, address = server_socket.accept()
#         print ("I got a connection from ", address)
#         while 1:
#             data = input('SEND( TYPE q or Q to Quit):')
#             if(data == 'Q' or data == 'q'):
#                 client_socket.send (data.encode())
#                 client_socket.close()
#                 break;
#             else:
#                 client_socket.send(data.encode())
#
#             data = client_socket.recv(512).decode()
#             if(data == 'q' or data == 'Q'):
#                 client_socket.close()
#                 break;
#             else:
#                 print ("RECEIVED:" , data)
#         break;
#     server_socket.close()
#     print("SOCKET closed... END")
#
#     #TCP Client Code:
#     # TCP client example
#     import socket
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect(("www.hsd.or.kr", 5000))
#     while 1:
#         data = client_socket.recv(512).decode()
#         if ( data == 'q' or data == 'Q'):
#             client_socket.close()
#             break;
#         else:
#             print ("RECEIVED:" , data)
#             data = input ( "SEND( TYPE q or Q to Quit):" )
#             if ( data == 'q' or data == 'Q'):
#                 client_socket.send(data.encode())
#                 client_socket.close()
#                 break;
#             else:
#                 client_socket.send(data.encode())
#     print ("socket colsed... END.")
