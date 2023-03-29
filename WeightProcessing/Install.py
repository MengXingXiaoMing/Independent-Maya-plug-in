#coding=gbk
import os
import inspect
import pymel.core as pm
cur_dir = '\\'.join(os.path.abspath(inspect.getsourcefile(lambda: 0)).split('\\')[:-1])  # 获取当前绝对路径的上层目录 linux中应用'/'split和join
file_path = os.path.join(cur_dir)  # 获取文件路径
cur_dirA = '/'.join(os.path.abspath(inspect.getsourcefile(lambda: 0)).split('\\')[:-1])
file_pathA = os.path.join(cur_dirA)  # 获取文件路径A
pm.melGlobals.initVar('string', 'gShelfTopLevel')
currentShelf=str(pm.tabLayout(pm.melGlobals['gShelfTopLevel'], query=1, selectTab=1))
pm.setParent(currentShelf)
pm.shelfButton(sourceType='python',
	image=(file_pathA+'/WeightIcon.png'),
	label='权重处理',
	iol=(''),
	command=('import sys\nsys.path.append(\"'+file_path+'\")\nimport WeightProcessing\nfrom WeightProcessing import *\nZKM_QvanZhongChuLiWindowClass().ZKM_WindowQvanZhongChuLiWindow()'),
	image1=(file_pathA+'/WeightIcon.png'),
	annotation='权重处理')
