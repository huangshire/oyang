import os

def create_path(path_name):
	if os.path.exists(path_name) is False:
		os.mkdir(path_name)

def list_path():
	path_list=[]
	temp_list=os.listdir()
	for i in temp_list:
		if os.path.isdir(i):
			print(i)
			path_list.append(i)
	return path_list
def list_file():
	file_list=[]
	temp_list=os.listdir()
	for i in temp_list:
		if os.path.isfile(i):
			print(i)
			file_list.append(i)
	return file_list
# create_path('jiaya')
list_path()
print('###'*15)
list_file()