class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self)==0

    def __len__(self):
        return len(self.items)

    def peek(self):
        assert not self.isEmpty()
        return self.items[-1]

    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()

    def push(self, data):
        self.items.append(data)

##PROMPT = 'Masukkan bilangan positif (<0 untuk mengakhiri): '
##myStack = Stack()
##value = int(input(PROMPT))
##while value >= 0:
##    myStack.push(value)
##    value = int(input(PROMPT))
##while not myStack.isEmpty():
##    value = myStack.pop()
##    print (value)

class StackLL(object):
    def __init__(self):
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.top is None

    def __len__(self):
        return self.size

    def peek(self):
        assert not self.isEmpty()
        return self.top.item

    def pop(self):
        assert not self.isEmpty()
        node = self.top
        self.top = self.top.next
        self.size -= 1
        return node.item

    def push(self, data):
        self.top = _StackNode(data, self.top)
        self.size += 1

class _StackNode(object):
    def __init__(self, data, link):
        self.item = data
        self.next = link


def cetakBiner(d):
    f = StackLL()
    if d==0:
        f.push(0)
    while d != 0:
        sisa = d%2
        d = d//2
        f.push(sisa)
    st = ""
    for i in range(len(f)):
        st = st + str(f.pop())
    return st

print ("Biner :",cetakBiner(12))

print ("\n==[NO_1]==")
def cetakHexa(n):
    f = Stack()
    if n == 0:
        f.push(0)
    while n != 0:
        sisa = n%16
        if sisa == 10:
            f.push('A')
            n = n//16
        elif sisa == 11:
            f.push('B')
            n = n//16
        elif sisa == 12:
            f.push('C')
            n = n//16
        elif sisa == 13:
            f.push('D')
            n = n//16
        elif sisa == 14:
            f.push('E')
            n = n//16
        elif sisa == 15:
            f.push('F')
            n = n//16
        else:
            f.push(sisa)
            n = n//16

    st = ""
    for i in range(len(f)):
        st = st + str(f.pop())
    return st

print ("Hexa :",cetakHexa(31519))

print ("\n==[NO_2]==")
nilai = Stack()
for i in range(16):
    if i % 3 == 0:
        nilai.push(i)
        print (nilai.items)

print ("\n==[NO_3]==")
nilai = Stack()
for i in range(16):
    if i % 3 == 0:
        nilai.push(i)
        print (nilai.items)
    elif i % 4 == 0:
        print(nilai.pop())
