queue=[]
def add(value):
    queue.append(value)
def sub():
    if not empty():
        del queue[0]
    else:
        return None
def empty():
    return len(queue)==0
def display():
    if len(queue)!=0:
        for i in queue:
            print(i)
    elif len(queue)==0:
        print('Stack is empty')
