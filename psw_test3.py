i=3
password = 'a123456'
while i > 0:
	psw = input('請輸入密碼: ')
	if psw == password:
		print('登入成功')
		break;
	else:
		i = int(i) - 1
		print('密碼錯誤! 還有', i, '次機會')