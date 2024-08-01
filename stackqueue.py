#stack 
stack=[]
stack.append("apple")
stack.append("cherry")
print("initial stack")
print(stack)
print("\n stack after elements are popped:")
print(stack)

#stack workout
my_stack=[]
my_stack.append("x")
my_stack.append("y")
my_stack.append("z")
print("\n stack after elements are popped:")
print(my_stack)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print("\n stack after elements are popped:")
print(my_stack)

#queue
queue=["apple","mango","cherry","banana"]
queue.append("kiwi")
queue.append("dragon")
print(queue)
print(queue.pop())
print(queue)
print(queue.pop())
print(queue)

#queue using list
queue=["dog","cat","elephant","lion"]
queue.append("tiger")
queue.append("cheeta")
print(queue)
print(queue.pop())
print(queue)
print(queue.pop())
print(queue)

file=open("new.txt","a")
file.write("hello world")
file.write("hii bhavya")
file.write("\n this \n will \n add \n this \n line")
file=open("new.txt","r")
print(file.read(19))
file.close()