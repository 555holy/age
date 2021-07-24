while True:
	driving = input('請問你有沒有開過車？')
	
	if driving == '有':
		age = int(input('請問你的年齡？'))
		if age >= 18:
			print('你考過駕照了')
		else:
			print('你完蛋了')
		break
	
	elif driving == '無':
		age = int(input('請問你的年齡？'))
		if age >= 18:
			print('太嫩了吧')
		else:
			print('好險你沒開過')	
		break
	else:
		print('不要瞎掰好嗎')
	

	
		

