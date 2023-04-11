from collections import deque
dq = deque('abc')
dq.append('d')
dq.appendleft('z')
dq.extend('pranav')
dq.extendleft('poudyal')
print(dq.pop())
print(dq.popleft())
print(dq)
dq.rotate(-2)
print(dq)
dq2 = deque([],maxlen=3)

for i in range(6):
    dq2.append(i)
    print(dq2)