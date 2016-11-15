# namedtuple()

t1 = ('hong', 23, 'female')
print(t1)

t2 = ('kang', 33, 'female')
print(t2)

for n in [t1, t2]:
	print('%s is %d age, %s' % n)


import collections

Person = collections.namedtuple("Person", 'name age gender')

p1 = Person(name="choi", age=28, gender="female")
p2 = Person(name="park", age=29, gender="female")

for n in [p1, p2]:
	print("%s is %d, %s" % n)


# OrderedDict : 데이터의 순서를 기억하는 사전형 클래스
# 일반  dict와 ordered 의 차이는 순서까지 같아야 비교시 같은 값이라고 판단.
d1 = {}  # 빈 dictionary
d1["key1"] = "value1"
d1["key2"] = "value2"
d1["key3"] = "value3"

for k, v in d1.items():
	print(k, v)


od1 = collections.OrderedDict()
od1['k1'] = 'v1'
od1['k2'] = 'v2'
od1['k3'] = 'v3'
od1['k4'] = 'v4'
od1['k5'] = 'v5'

for k, v in od1.items():
	print(k, v)





