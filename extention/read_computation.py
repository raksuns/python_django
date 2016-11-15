import json

datas = None

try:
	with open('nanum.json') as jsonData:
		datas = json.load(jsonData)

	print('key length : ', len(datas))
	for key in datas.keys():
		print(key, ' : ', datas[key])

except IOError as e:
	print('File Error')


