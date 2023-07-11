import win32com.client
    
class Mail():

     def __init__(self):
         self.ol=win32com.client.Dispatch("outlook.application")
         pass
     
     def sendMail(self, receiver,body):
        
        newmail=self.ol.CreateItem(0)
        newmail.Subject= 'Raw materials key access'
        newmail.To= receiver 
        newmail.Body= 'Hello, this is your personal key for RFID Raw Materials mobile app : '+ body
        newmail.Display(True)