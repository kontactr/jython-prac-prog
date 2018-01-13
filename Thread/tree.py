import threading

lock = threading.Lock()

class Node():

    def __init__(self,data=None,left=None,right=None):
        self.left = left
        self.data = data
        self.right = right

    def update_data(self,data):
        lock.acquire()
        self.data = data
        lock.release()

    def update_right(self,right):
        lock.acquire()
        self.right = right
        lock.release()

    def update_left(self,left):
        lock.acquire()
        self.left = left
        lock.release()

    def update_all(self,data=None,left=None,right=None):
        if (data != None):
            self.update_data(data)
        if (left != None):
            self.update_left(left)
        if (right != None):
            self.update_right(right)


    def traversal(self,node=None):
        tra_list = []
        data = []
        if node == None:
            data.append(self.data)
            tra_list.extend([self.left,self.right])
        else:
            data.append(node.data)
            tra_list.extend([node.left,node.right])

        while (len(tra_list) != 0):
            ele_pop = tra_list.pop(0)
            if ele_pop == None:
                pass
            else:
                tra_list.extend([ele_pop.left,ele_pop.right])
                data.append(ele_pop.data)
        tra_list.clear()
        print (data)


n1 = Node(data=10)
n2 = Node(data=20)
n3 = Node(data=30)
n4 = Node(data=40)
n1.update_right(n3)
n1.update_left(n2)
n2.update_left(n4)
t1 = threading.Thread(target=n1.traversal,args=[])
t2 = threading.Thread(target=n2.traversal,args=[])

t1.start()
t2.start()
t1.join()
t2.join()


        
        
