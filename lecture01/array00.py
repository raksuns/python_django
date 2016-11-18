# pprint(pretty print)

from pprint import pprint
import array

pprint({})

# array


str = "abcdefghijk"

arr = array.array("u", str)
print(arr)
print(array.typecodes) # typecodes를 이용하면 어떠한 캐릭터 타입을 사용할수 있는지

arr1 = array.array('i', range(5))
print(arr1)

arr1.extend(range(5))
print(arr1)

print(arr1[3:6])
print(arr1)

al = list(enumerate(arr1))
print(al)




