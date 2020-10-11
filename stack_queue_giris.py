from _collections import deque

l = [0,1,2,3,4]         #stack(yığın) yapısı ise böyle tanımlanmaktadır.
l.append(55)
print(l.pop())
print(l.pop())
print(l)
#stack yapısında son giren ilk çıkar ancak queue yapısında ıse son giren ilk çıkar.
#stack
l1= deque([0,1,2,3,4])       #queue yığını böyle tanımlanmaktadır.
print(l1.popleft())
print(l1)