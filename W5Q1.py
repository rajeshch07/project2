class cars:
    def cardeets(self):
        self.ownername=input("Enter name: ")
        self.car=input("Enter car brand/model: ")
    def display(self):
        print(self.ownername, self.car)
cardeets_list=[]
while(True):
    c1=cars()
    c1.cardeets()
    cardeets_list.append(c1)
    ch=input("Add more students details Y/N ")
    if (ch == 'N'):
       break
for i in cardeets_list:
    i.display()
            
