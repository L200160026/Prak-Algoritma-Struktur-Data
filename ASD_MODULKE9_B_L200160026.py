#Author : Ridwan Renaldi (L200160026)
#Kelas : B
#Python 3.6

class Queue(object):
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.qlist)

    def enqueue(self, data):
        self.qlist.append(data)

    def dequeue(self):
        assert not self.isEmpty()
        return self.qlist.pop(0)

    def getFrontMost(self):
        return self.qlist[0]

    def getRearMost(self):
        return self.qlist[-1]

Q = Queue()
Q.enqueue(28)
Q.enqueue(19)
Q.enqueue(45)
Q.enqueue(13)
Q.enqueue(7)

##print ("Paling Depan :",Q.getFrontMost())
##print ("Paling Belakang :",Q.getRearMost())
##
##print (Q.dequeue())
##print (Q.dequeue())
##print (Q.dequeue())
##print (Q.dequeue())
##print (Q.dequeue())

class PriorityQueue(object):
    def __init__(self):
        self.qlist = []

    def __len__(self):
        return len(self.qlist)

    def isEmpty(self):
        return len(self) == 0

    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)

    def dequeue(self):
        assert not self.isEmpty()
        prioritas = self.qlist[0].priority
        ppop = 0
        for i in range(len(self.qlist)):
            if self.qlist[i].priority < prioritas:
                prioritas = self.qlist[i].priority
                ppop = i
        return self.qlist.pop(ppop)
            

    def getFrontMost(self):
        return self.qlist[0]

    def getRearMost(self):
        return self.qlist[-1]

class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

S = PriorityQueue()
S.enqueue("Jeruk", 4)
S.enqueue("Tomat", 2)
S.enqueue("Mangga", 0)
S.enqueue("Duku", 5)
S.enqueue("Pepaya", 2)
print(S.dequeue().item)
print(S.dequeue().item)
print(S.dequeue().item)

