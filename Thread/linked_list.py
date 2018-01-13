class linked_list:

    def __init__(self,data=None,link=None):
        self.data=data
        self.link=link

    def update_data(self,data):
        self.data = data

    def update_link(self,link):
        self.link = link

    def insert(self):
        temp = self
        while temp.link!= None:
                print (temp.link)
                temp = temp.link
        obj = linked_list(data=input())
        print (obj)
        temp.link = obj

    def traversal(self):
        temp = self
        while temp.link != None:
            print (temp.data)
            temp = temp.link
        print (temp.data)


root = linked_list(data=20)
root.insert()
#print (root.link)
#print (root.link.link)
root.insert()
#print (root.link)
#print (root.link.link)
root.traversal()
        
            
