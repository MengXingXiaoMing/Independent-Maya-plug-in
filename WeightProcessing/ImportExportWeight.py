#coding=gbk
import os
import inspect
from os import listdir
import pymel.core as pm
cur_dirA = '/'.join(os.path.abspath(inspect.getsourcefile(lambda: 0)).split('\\')[:-1])
file_pathA = os.path.join(cur_dirA)  # 获取文件路径
cur_dirB = '\\'.join(os.path.abspath(inspect.getsourcefile(lambda: 0)).split('\\')[:-1])
file_pathB = os.path.join(cur_dirB)  # 获取文件路径
def ExportWeight():
    Model = pm.ls(sl=1)
    if any(name.endswith(('.xml')) for name in os.listdir(file_pathA + '/ImportExportWeights/')):
        my_path = (file_pathA + '/ImportExportWeights/')
        for file_name in listdir(my_path):
            if file_name.endswith('.xml'):
                os.remove(my_path + file_name)
            if file_name.endswith('.txt'):
                os.remove(my_path + file_name)
    for MD in Model:
        pm.select(MD, r=1)
        Joint = pm.skinCluster(q=1, inf=1)
        file = open((file_pathB+'\ImportExportWeights\\'+MD+'.txt'), "w")
        for Jon in Joint:
            file.write(Jon+'\n')
        file.close()
def ImportWeight():
    Model=pm.ls(sl=1)
    AllNodes = pm.ls(type='joint')
    for MD in Model:
        fo = open(file_pathB+"\ImportExportWeights\\"+MD+".txt","r")
        lines = [l.split() for l in fo if l.strip()]
        fo.close()
        for i in range(0, len(lines)):
            lines[i] = (str(lines[i])[2:-2])
        addJoint = [x for x in lines if x not in AllNodes]  # 筛选出需要补充创建的骨骼
        #print(addJoint)
        for J in addJoint:#补充骨骼
            pm.select(cl=1)
            pm.joint(p=(0, 0, 0), n=J)
        HaveSkinCluster = str(pm.mel.findRelatedSkinCluster(MD))#查询是否有蒙皮节点
        if (len(HaveSkinCluster)>0):
            pm.select(MD, r=1)
            pm.mel.eval('DetachSkin;')
        pm.select(lines, r=1)
        pm.select(MD, add=1)
        pm.mel.eval('SmoothBindSkin;')
        SkinCluster = str(pm.mel.findRelatedSkinCluster(MD))  # 查询蒙皮节点
        pm.deformerWeights((MD+ ".xml"),
                           path=(file_pathA + "/ImportExportWeights/"), im=1, method="index",
                           deformer=SkinCluster)
        #pm.skinCluster(SkinCluster, forceNormalizeWeights=1, e=1)


#print(file_pathA+'/ImportExportWeights/')



