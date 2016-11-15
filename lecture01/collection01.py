"""
[collections module]
Counter : 컨테이너에 동일한 값의 자료가 몇개인지를 파악하는데 사용하는 함수

"""

import collections

print(collections.Counter(["aa", "cc", "dd", "aa", "bb", "ee"]))
print(collections.Counter({"가": 3, "나": 2, "다": 4}))
print(collections.Counter(a=2, b=4, c=1))

container = collections.Counter()
print(container)

container.update("aabbccddggff")
print(container)

container.update({'c': 2, 'f': 3})
print(container)

# Counter 접근하기
for n in "abcdef":
	print("%s: %d" % (n, container[n]))

ct = collections.Counter("Hello jenny")
ct['x'] = 0

print(ct)
print('list : ', list(ct.elements()))

# most_common() : 상위 n 개를 시퀀스로 만든다.
ct2 = collections.Counter()
with open('test.txt', 'rt') as f:
	for line in f:
		ct2.update(line.rstrip().lower())

for item, cnt in ct2.most_common(5):  # ct2에 저장된 값에서 빈도수가 많은 상위 n개의 값을 가져온다.
	print("%s : %2d" % (item, cnt))

print(ct2.most_common())


# Counter 객체는 산술/집합 연산이 가능하다.
ct3 = collections.Counter(['a', 'b', 'c', 'd', 'a', 'f', 'c'])
ct4 = collections.Counter("aaaeroplane")

print(ct3)
print(ct4)

print(ct3 + ct4)
print(ct3 - ct4)
print(ct3 & ct4)  # 교집합
print('union : ', ct3 | ct4)  # 최대값만 출력

# defaultdict
def default_fuc1():
	return "aa"
dic = collections.defaultdict(default_fuc1, n1="hi yo")
print(dic)
print(dic['n1'])
print(dic['n2'])  # 컨테이너를 초기화할 때 디폴드 값을 지정 한다. 키에 대한 값일 없을 경우 디폴트값 리턴됨















