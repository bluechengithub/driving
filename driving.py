country = input ('請問你的國家是: ')
age = input('請問你的年齡是: ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你不能考駕照')
elif country == '美國':
	if age >= 16:
		print('你可以在美國考駕照')
	else:
 		print('你不能在美國考駕照')
else:
	print('沒有在資料庫')