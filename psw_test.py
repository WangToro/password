i=3
password = 'a123456'
while True:
	psw = input('請輸入密碼: ')
	if psw == password:
		print('登入成功')
		break;
	else:
		i = int(i) - 1
		if int(i) == 0:
			break;
		else:
			print('密碼錯誤! 還有', i, '次機會')