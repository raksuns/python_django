# 힙 정렬 알고리즘
# 2진 트리로 구성 후 트리에서 큰수를 기준으로 위로 올린다. 가장 큰수는 따로 보관되고,
# 다음 가장 큰 수를 찾기 위해 다시 이진 트리에서 큰수를 위로 올린다.
# 탐색은 아래에서 부터 하면 큰수를 비교된 큰수가 상위로 올라가는 구조.
# heap : tree 형태의 자료 구조
# heapq
"""
heap 이란 자식 노드가 부모노드와 정렬관계를 가지는 트리형 자료 구조
max-heap : 큰값이 위로 (부모가 자식보다 크거나 같다
min-heap : 작은 값이 위로 - python 에서 제공하는 heap (부모가 자식과 같거나 작다.

이진 힙의 경우 array나 list를 사용해서 표현할 수 있다. 인덱스를 이용해서 수식으로 표시할 수 있다.)
수식은  n을 부모로하는 자식 노드의 위치 수식은 (2*n+1, 2*n+2) (left node, right node)

"""

import heapq

data = [10, 8, 5, 4, 6, 9]

heap = []

for n in data:
	heapq.heappush(heap, n)

heapq.heapify(data)  # heap push 보다 간단하게 정렬된 heap을 생성한다

# heap 데이터 접근하기 : heappop()을 이용하여 가장 작은 값을 하나씩 끄집어 낸다.

for n in range(3):
	min_val = heapq.heappop(data)
	print(min_val, end=',')


print('\n####')
# heap 데이터 수정 : heapreplace
data = [10, 8, 5, 4, 6, 9]
min_val = heapq.heapreplace(data, 15)
print(min_val, end='\n')
for n in range(len(data)):
	min_val = heapq.heappop(data)
	print(min_val, end=',')

print(min_val, end='\n')
# heap의 최대 / 최소 값 구하기 : nlargest(), nsmallest()
data = [10, 8, 5, 4, 6, 9]
print(heapq.nlargest(6, data))
print(heapq.nlargest(3, data))
print(heapq.nsmallest(6, data))
print(heapq.nsmallest(3, data))