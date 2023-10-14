
      
    class User:
    def __init__ (self, username, password):
        self.username = username
        self.password = password

class Buyer (User):
    def __init__ (self, username, password, address, national_code):
        super(). __init__ (username, password)
        self.address = address
        self.national_code = national_code

    def print_info(self):
        print("Username:", self.username)
        print("Password:", self.password)
        print("Address:", self.address)
        print("National Code:", self.national_code)
     buyer = Buyer("maryam", "maryam4203", "123 Main St", "4200368171")
buyer.print_info()
        
