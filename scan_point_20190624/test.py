def read_file(name):
	with open(name ,'r') as fn:
		temp=fn.read()
	return temp
name=r'聚丙烯\聚合.txt'
print(read_file(name))

"""我们的世界，是一个美丽的世界。
对酒当歌，人生几何。
譬如朝露，去日苦多。
慨当以慷，忧思难忘。
何以解忧，惟有杜康。
青青子衿，悠悠我心。
但为君故，沉吟至今。"""
