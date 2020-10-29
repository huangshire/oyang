#base64

test_text='192.168.28.143#auto#0'

def take_inverse(date):
	out_date=''
	# print(len(date))
	if len(date)<=8:
		for i in range(8-len(date)):
			date='0'+date
	elif len(date)>8 and len(date)<=16:
		for i in range(16-len(date)):
			date='0'+date
	for a in date:
		if a=='1':
			out_date+='0'
		else:
			out_date+='1'

	return out_date

def two2ten(date):
	out_num=0
	for i in range(len(date)):
		out_num+=int(date[i])*2**i
	return out_num
def ten2two(date):
	temp=bin(ord(date)).replace('0b','')
	return temp
#print(~
def save_file(name,date):
	save_date=encryption(date)
	with open(name,'w',encoding='utf-8') as fn:
		fn.write(save_date)
def read_file(name):
	with open(name,'r',encoding='utf-8') as fn:
		read_temp=fn.read()
		read_date=encryption(read_temp)
	return read_date
def encryption(text):
	#test_date='1'
	encry_test=''
	for test_date in text:
		buff_date=ten2two(test_date)
		# print(buff_date)
		result=take_inverse(buff_date)
		# print(result)
		char_date=two2ten(result)
		# print(char_date)
		encry_test+=chr(char_date)
	#save_file(encry_test)
	#print(encry_test)
	return encry_test
# print(asc_date)
# print(chr('0b'+result))
if __name__ == '__main__':
	# encryp_in=encryption(test_text)
	#encryp_in=encryption(test_text)
	# print(encryp_in)
	save_file('test_text.txt',test_text)
	temp=read_file('test_text.txt')
	# encryp_out=encryption(temp)
	print(temp)
