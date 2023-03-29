#coding=gbk
import os
import inspect
import pymel.core as pm
cur_dirA = '/'.join(os.path.abspath(inspect.getsourcefile(lambda: 0)).split('\\')[:-1])
file_pathA = os.path.join(cur_dirA)  # 获取文件路径A
pm.melGlobals.initVar('string', 'gShelfTopLevel')
currentShelf=str(pm.tabLayout(pm.melGlobals['gShelfTopLevel'], query=1, selectTab=1))
pm.setParent(currentShelf)
pm.shelfButton(sourceType='python',
	image=(file_pathA+'/WeightIcon.png'),
	label='权重处理',
	iol=(''),
	command=('import maya.app.general.executeDroppedPythonFile as myTempEDPF\nmyTempEDPF.executeDroppedPythonFile(\"'+file_pathA+'/WeightProcessing.py\", \"\")\ndel myTempEDPF\nprint()'),
	image1=(file_pathA+'/WeightIcon.png'),
	annotation='权重处理')
pm.shelfButton(sourceType='mel',
	image=(file_pathA+'/WeightIcon.png'),
	label='权重处理',
	iol=(''),
	command=('source \"'+file_pathA+'/权重处理.mel";'),
	image1=(file_pathA+'/WeightIcon.png'),
	annotation='权重处理')
print()