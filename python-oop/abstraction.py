# reduce complexity by hiding unecessary details/ hiding abstraction.
# abstraction- focuses more on simplifying usage by hiding unnecessary details

class EmailService:
    def _connect(self):
        print(f"connectiong to email server")
    def _authenticate(self):
        print("authenticating") 
    def send_email(self):
        self._connect()  
        self._authenticate()
        print("sending email")
        self._disconnect()
    def _disconnect(self):
        print("disconnecting from email server....")    
email= EmailService()    
email.send_email()