# _*_ coding:utf-8 _*_

import tkinter
import tkinter.font as tkFont 
import socket
import threading
import time
import sys

class ServerUI():
    
    title = 'Python在线聊天-服务器端V1.0'
    local = '127.0.0.1'
    port = 5505
    global serverSock;
    flag = False

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title(self.title)
        
        self.frame = [tkinter.Frame(),tkinter.Frame(),tkinter.Frame(),tkinter.Frame()]

        self.chatTextScrollBar = tkinter.Scrollbar(self.frame[0])
        self.chatTextScrollBar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        
        ft = tkFont.Font(family='Fixdsys',size=11)
        self.chatText = tkinter.Listbox(self.frame[0],width=70,height=18,font=ft)
        self.chatText['yscrollcommand'] = self.chatTextScrollBar.set
        self.chatText.pack(expand=1,fill=tkinter.BOTH)
        self.chatTextScrollBar['command'] = self.chatText.yview()
        self.frame[0].pack(expand=1,fill=tkinter.BOTH)
        
        label = tkinter.Label(self.frame[1],height=2)
        label.pack(fill=tkinter.BOTH)
        self.frame[1].pack(expand=1,fill=tkinter.BOTH)
        
        self.inputTextScrollBar = tkinter.Scrollbar(self.frame[2])
        self.inputTextScrollBar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        
        ft = tkFont.Font(family='Fixdsys',size=11)
        self.inputText = tkinter.Text(self.frame[2],width=70,height=8,font=ft)
        self.inputText['yscrollcommand'] = self.inputTextScrollBar.set
        self.inputText.pack(expand=1,fill=tkinter.BOTH)
        self.inputTextScrollBar['command'] = self.chatText.yview()
        self.frame[2].pack(expand=1,fill=tkinter.BOTH)
        
        self.sendButton=tkinter.Button(self.frame[3],text=' 发 送 ',width=10,command=self.sendMessage)
        self.sendButton.pack(expand=1,side=tkinter.BOTTOM and tkinter.RIGHT,padx=25,pady=5)

        self.closeButton=tkinter.Button(self.frame[3],text=' 关 闭 ',width=10,command=self.close)
        self.closeButton.pack(expand=1,side=tkinter.RIGHT,padx=25,pady=5)
        self.frame[3].pack(expand=1,fill=tkinter.BOTH)
        
    def receiveMessage(self):
        self.serverSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serverSock.bind((self.local,self.port))
        self.serverSock.listen(15)
        self.buffer = 1024
        self.chatText.insert(tkinter.END,'服务器已经就绪......')

        while True:
            self.connection,self.address = self.serverSock.accept()
            self.flag = True
            while True:
               
                self.cientMsg = self.connection.recv(self.buffer).decode('utf-8')
                if not self.cientMsg:
                    continue
                elif self.cientMsg == 'Y':
                    self.chatText.insert(tkinter.END,'服务器端已经与客户端建立连接......')
                    self.connection.send(b'Y')
                elif self.cientMsg == 'N':
                    self.chatText.insert(tkinter.END,'服务器端与客户端建立连接失败......')
                    self.connection.send(b'N')
                else:
                    theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    self.chatText.insert(tkinter.END, '客户端 ' + theTime +' 说：\n')
                    self.chatText.insert(tkinter.END, '  ' + self.cientMsg)
    

    def sendMessage(self):

        message = self.inputText.get('1.0',tkinter.END)
       
        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.chatText.insert(tkinter.END, '服务器 ' + theTime +' 说：\n')
        self.chatText.insert(tkinter.END,'  ' + message + '\n')
        if self.flag == True:
          
            self.connection.send(message.encode())
        else:
            
            self.chatText.insert(tkinter.END,'您还未与客户端建立连接，客户端无法收到您的消息\n')
       
        self.inputText.delete(0.0,message.__len__()-1.0)
    
    
    def close(self):
        sys.exit()
    
    def startNewThread(self):
        thread=threading.Thread(target=self.receiveMessage,args=())
        thread.setDaemon(True);
        thread.start();
    
def main():
    server = ServerUI()
    server.startNewThread()
    server.root.mainloop()
    
if __name__=='__main__':
    main()

