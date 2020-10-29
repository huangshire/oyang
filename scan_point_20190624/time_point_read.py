def read_time_point():
	with open('time_point.txt','r') as fn:
		time_point_temp=fn.read()
	club_qita=[]
	club_banzhang=[]
	for i in time_point_temp.split('\n')[0].split('#'):
		club_qita.append(i.split(','))
	for j in time_point_temp.split('\n')[1].split('#'):
		club_banzhang.append(j.split(','))
	return club_qita,club_banzhang
if __name__ == '__main__':
	
	club_qita,club_banzhang=read_time_point()
	print(club_qita,'\n',club_banzhang)