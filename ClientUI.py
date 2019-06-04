# _*_ coding:utf-8 _*_

import tkinter
import tkinter.font as tkFont 
import socket
import threading
import time
import sys

class ClientUI():
    
    title = 'Python在线聊天-客户端V1.0'
    local = '127.0.0.1'
    port = 5505
    global clientSock;
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
        self.sendButton.pack(expand=1,side=tkinter.BOTTOM and tkinter.RIGHT,padx=15,pady=8)

        self.closeButton=tkinter.Button(self.frame[3],text=' 关 闭 ',width=10,command=self.close)
        self.closeButton.pack(expand=1,side=tkinter.RIGHT,padx=15,pady=8)
        self.frame[3].pack(expand=1,fill=tkinter.BOTH)
        

    def receiveMessage(self):
        try:
            self.clientSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.clientSock.connect((self.local, self.port))
            self.flag = True
        except:
            self.flag = False
            self.chatText.insert(tkinter.END,'您还未与服务器端建立连接，请检查服务器端是否已经启动')
            return
            
        self.buffer = 1024
        self.clientSock.send('Y'.encode())
        while True:
            try:
                if self.flag == True:
                    self.serverMsg = self.clientSock.recv(self.buffer).decode('utf-8')
                    if self.serverMsg == 'Y':
                        self.chatText.insert(tkinter.END,'客户端已经与服务器端建立连接......')
                    elif self.serverMsg == 'N':
                        self.chatText.insert(tkinter.END,'客户端与服务器端建立连接失败......')
                    elif not self.serverMsg:
                        continue
                    else:
                        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        self.chatText.insert(tkinter.END, '服务器端 ' + theTime +' 说：\n')
                        self.chatText.insert(tkinter.END, '  ' + self.serverMsg)
                else:
                    break
            except EOFError as msg:
                raise msg
                self.clientSock.close()
                break
                  
    def sendMessage(self):
        message = self.inputText.get('1.0',tkinter.END)
        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.chatText.insert(tkinter.END, '客户端器 ' + theTime +' 说：\n')
        self.chatText.insert(tkinter.END,'  ' + message + '\n')
        if self.flag == True:
            self.clientSock.send(message.encode());
        else:
            self.chatText.insert(tkinter.END,'您还未与服务器端建立连接，服务器端无法收到您的消息\n')
        self.inputText.delete(0.0,message.__len__()-1.0)
    
    def close(self):
        sys.exit()
    
    def startNewThread(self):
        thread=threading.Thread(target=self.receiveMessage,args=())
        thread.setDaemon(True);
        thread.start();

def main():
    client = ClientUI()
    client.startNewThread()
    client.root.mainloop()
    
if __name__=='__main__':
    main()

