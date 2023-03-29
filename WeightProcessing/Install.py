#coding=gbk
import os
import inspect
import pymel.core as pm
cur_dirA = '/'.join(os.path.abspath(inspect.getsourcefile(lambda: 0)).split('\\')[:-1])
file_pathA = os.path.join(cur_dirA)  # ��ȡ�ļ�·��A
pm.melGlobals.initVar('string', 'gShelfTopLevel')
currentShelf=str(pm.tabLayout(pm.melGlobals['gShelfTopLevel'], query=1, selectTab=1))
pm.setParent(currentShelf)
pm.shelfButton(sourceType='python',
	image=(file_pathA+'/WeightIcon.png'),
	label='Ȩ�ش���',
	iol=(''),
	command=('import maya.app.general.executeDroppedPythonFile as myTempEDPF\nmyTempEDPF.executeDroppedPythonFile(\"'+file_pathA+'/WeightProcessing.py\", \"\")\ndel myTempEDPF\nprint()'),
	image1=(file_pathA+'/WeightIcon.png'),
	annotation='Ȩ�ش���')
pm.shelfButton(sourceType='mel',
	image=(file_pathA+'/WeightIcon.png'),
	label='Ȩ�ش���',
	iol=(''),
	command=('source \"'+file_pathA+'/Ȩ�ش���.mel";'),
	image1=(file_pathA+'/WeightIcon.png'),
	annotation='Ȩ�ش���')
print()