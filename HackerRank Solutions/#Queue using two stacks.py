#Queue using two stacks 
# Enter your code here. Read input from STDIN. Print output to STDOUT
# stackpush - 
# stackdelete - 78 60

q = int(input())
stackpush = []
stackdelete = []
for i in range(q):
    t = list(input().split())
    if t[0] == '1':
        stackpush.append(t[1])
        
    
    # dequeue
    elif t[0] == '2':
        if not stackdelete:
            while stackpush:
                stackdelete.append(stackpush.pop())
        stackdelete.pop()
        
    # print the front element
    else:
        if not stackdelete:
            while stackpush:
                stackdelete.append(stackpush.pop())
        print(stackdelete[-1])   
