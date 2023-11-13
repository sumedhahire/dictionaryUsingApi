
class Qclass:
    def __init__(self,size):
        self.Qobj=[]
        self.size=size
    def put(self,data):
        if len(self.Qobj)==self.size:
            self.Qobj.remove(self.Qobj[0])
        self.Qobj.append(data)

    def get(self):
        self.Qobj.reverse()
        return self.Qobj
    
    def size(self):
        return len(self.Qobj)

q=Qclass(5)

print(q.get())

q.put(30)
q.put(20)
print(q.get())