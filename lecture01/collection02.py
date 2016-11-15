# Deque : 양방향 큐

import collections

deq = collections.deque("abcdefe hijklmn opqrstu wxyz")

print(deq)
print(len(deq))
print(deq[0])
print(deq[-2])

deq.remove('w')
print(deq)

deq.append('w')
print(deq)

deq.appendleft('0')
print(deq)

deq.extendleft('1')
print(deq)

deq1 = collections.deque()
deq1.extend('abcdefg')
deq1.append('A')
print(deq1)
deq1.extendleft('F')
print(deq1)

deq1.pop()
print(deq1)

deq1.popleft()
print(deq1)

while True:
	try:
		print(deq1.popleft(), end=', ')
	except IndexError:
		break


