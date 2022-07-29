class stackADT:
    def __init__(self, size):
        self.size = size
        self.l = [None] * size
        self.top = -1

    def isFull(self):
        if self.top == self.size - 1:
            return 1
        else:
            return 0

    def isEmpty(self):
        if self.top == (-1):
            return 1
        else:
            return 0

    def Push(self,value):
        if self.isFull() == 1:
            print("The Stack is Full!!")
            print("\n")
        else:
            self.top += 1
            self.l[self.top] = value
            #print("Push operation is done!\n")

    def Pop(self):
        if self.isEmpty() == 1:
            print("The Stack is Empty!!")
            print("\n")
        else:
            k= self.l[self.top]
            self.l[self.top] = None
            self.top -= 1
            return k
            #print("Pop operation is done!\n")

    def Peek(self):
        if self.isEmpty() == 1:
            print("The Stack is Empty!!")
        else:
            print(self.l[self.top])

    def display(self):
        print(self.l)





    def add(self):
        a1=self.Pop()
        a2=self.Pop()
        b=a2+a1
        self.Push(b)

    def sub(self):
        a1 = self.Pop()
        a2 = self.Pop()
        b = a2 - a1
        self.Push(b)

    def mul(self):
        a1 = self.Pop()
        a2 = self.Pop()
        b = a2 * a1
        self.Push(b)

    def div(self):
        a1 = self.Pop()
        a2 = self.Pop()
        b = a2 / a1
        self.Push(b)

stack_size = int(input("Enter the size of the stack: "))
stack = stackADT(stack_size)
a=str(input("Enter an Expression : "))
a=a.split()
print(a)
digits=['0','1','2','3','4','5','6','7','8','9']
operator=['*','^','/','-','+']
no_of_digits=0
no_of_op=0
for i in a:
    if i in digits:
        no_of_digits+=1
    elif i in operator:
        no_of_op+=1
    else:
        pass

if no_of_digits== (no_of_op+1):

    for i in a:
        print(i)
        if i in digits:
            stack.Push(int(i))
            stack.display()
        elif i == '+':
            stack.add()
            stack.display()
        elif i == '-':
            stack.sub()
            stack.display()
        elif i == '*':
            stack.mul()
            stack.display()
        elif i == '/':
            stack.div()
            stack.display()


    print(stack.l[0])
else:
    print('Invalid postfix expression')
