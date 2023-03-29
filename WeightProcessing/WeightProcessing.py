#coding=gbk
import pymel.core as pm
import maya.cmds as cmds
from os import listdir
# 获取文件路径
import os
import inspect
# 加载文本
ZKM_RootDirectory = os.path.join('\\'.join(os.path.abspath(inspect.getsourcefile(lambda: 0)).split('\\')[:-5]))
class ZKM_QvanZhongChuLiWindowClass:
    def __init__(self):
        cur_dir = '\\'.join(
            os.path.abspath(inspect.getsourcefile(lambda: 0)).split('\\')[:-1])  # 获取当前绝对路径的上层目录 linux中应用'/'split和join
        file_path = os.path.join(cur_dir)  # 获取文件路径
        cur_dirA = '/'.join(
            os.path.abspath(inspect.getsourcefile(lambda: 0)).split('\\')[:-1])  # 获取当前绝对路径的上层目录 linux中应用'/'split和join
        file_pathReversion = os.path.join(cur_dirA)  # 获取文件路径A
        # 通过self向新建的对象中初始化属性
        self.file_path = file_path
        self.file_pathReversion = file_pathReversion
    def ZKM_WindowQvanZhongChuLiWindow(self):
        if pm.window('WindowQvanZhongChuLiPY', ex=1):
            pm.deleteUI('WindowQvanZhongChuLiPY')

        pm.window('WindowQvanZhongChuLiPY', t='权重处理')
        pm.columnLayout()
        pm.rowColumnLayout(nc=1, adj=1)
        pm.rowColumnLayout(nc=3, adj=3)
        pm.rowColumnLayout(nc=2, adj=3)
        pm.button(c='ZKM_QvanZhongChuLiCommandsClass().ZKM_ReadLoadText(\'textFieldButtonGrp\',\'XZKBY\')', l='选择拷贝源:')
        pm.textFieldButtonGrp('XZKBY', bl='加载', text='', cw3=(0, 100, 65), l='选择拷贝源:',
                              bc='ZKM_QvanZhongChuLiCommandsClass().ZKM_LoadText(\'textFieldButtonGrp\',\'XZKBY\')')
        pm.setParent('..')
        pm.rowColumnLayout(nc=2, adj=3)
        pm.button(c='ZKM_QvanZhongChuLiCommandsClass().ZKM_ReadLoadText(\'textFieldButtonGrp\',\'XZKBMXHD\')', l='选择需拷贝点:')
        pm.textFieldButtonGrp('XZKBMXHD', bl='加载', text='', cw3=(0, 100, 65), l='选择需拷贝点:',
                              bc='ZKM_QvanZhongChuLiCommandsClass().ZKM_LoadText(\'textFieldButtonGrp\',\'XZKBMXHD\')')
        pm.setParent('..')
        pm.button(c='ZKM_QvanZhongChuLiCommandsClass().ZKM_CopyPointWeightApply()', l='拷贝点权重')
        pm.rowColumnLayout(nc=2, adj=2)
        pm.button(c='pm.mel.CopyVertexWeights()', l='复制顶点权重')
        pm.button(c='pm.mel.PasteVertexWeights()', l='粘贴顶点权重')
        pm.button(c='pm.mel.RemoveUnusedInfluences()', l='移除无权重骨骼')
        #pm.button(c='ZKM_QvanZhongChuLiCommandsClass().AbsolutePositionMirrorWeight()', l='绝对位置镜像权重(停用)')
        pm.setParent('..')
        pm.rowColumnLayout(nc=7, adj=1)
        pm.iconTextButton(i='paintSkinWeights.png', flat=0, style='iconAndTextCentered',
                          c='pm.mel.ArtPaintSkinWeightsTool()', l='')
        pm.iconTextButton(flat=0, style='iconAndTextCentered', i='weightHammer.png', h=45,
                          c='pm.mel.weightHammerVerts()', l='')
        pm.iconTextButton(i='copySkinWeight.png', flat=0, style='iconAndTextCentered', c='pm.mel.CopySkinWeights()',
                          l='')
        pm.iconTextButton(i='mirrorSkinWeight.png', flat=0, style='iconAndTextCentered', c='pm.mel.MirrorSkinWeights()',
                          l='')
        pm.iconTextButton(i='moveSkinnedJoint.png', flat=0, style='iconAndTextCentered',
                          c='pm.mel.MoveSkinJointsTool()', l='')
        pm.iconTextButton(i='moveVertexWeights.png', flat=0, style='iconAndTextCentered',
                          c='pm.mel.artAttrMoveInfluence()', l='')
        pm.iconTextButton(i='showInfluence.png', flat=0, style='iconAndTextCentered',
                          c='pm.mel.artAttrShowInfluences(\'artAttrSkinPaintCtx\')', l='')
        pm.setParent('..')
        pm.rowColumnLayout(nc=1, adj=1)
        pm.button(c='ZKM_QvanZhongChuLiCommandsClass().ZKM_CopyModelWeightApply()', l='拷贝权重(先选源模型)')
        pm.button(c='ZKM_QvanZhongChuLiCommandsClass().ZKM_HalfCopyModelWeightApply()', l='对半拷贝权重')
        pm.setParent('..')
        pm.setParent('..')
        pm.rowColumnLayout(nc=3, adj=3)
        pm.optionMenu('NormalizeWeight', label='')
        pm.menuItem(label='后期')
        pm.menuItem(label='交互')
        pm.optionMenu('NormalizeWeight', edit=1, select=1)
        pm.intSliderGrp('SmoothWeightType', min=1, max=100, cw3=(60, 40, 258), f=1, fieldMaxValue=9999, l='平滑次数：', v=1)
        pm.button(c='ZKM_QvanZhongChuLiCommandsClass().ZKM_SmoothWeight()', l='平滑权重', w=60)
        pm.setParent('..')
        pm.rowColumnLayout(nc=4, adj=3)
        pm.button(c='ZKM_QvanZhongChuLiCommandsClass().ZKM_ReadLoadText(\'textFieldButtonGrp\',\'XZYMX\')', l='选择原模型:')
        pm.textFieldButtonGrp('XZYMX', bl='加载', bc='ZKM_QvanZhongChuLiCommandsClass().ZKM_LoadText(\'textFieldButtonGrp\',\'XZYMX\')')
        pm.button(c='ZKM_QvanZhongChuLiCommandsClass().ZKM_MergeWeightsToTargetsApply()', l='选择模型合并权重到目标')
        pm.button(c='ZKM_QvanZhongChuLiCommandsClass().ExportWeights()', l='导出权重')
        pm.button(c='ZKM_QvanZhongChuLiCommandsClass().ZKM_ReadLoadText(\'textFieldButtonGrp\',\'ZYQZ\')', l='选择模型:')
        pm.textFieldButtonGrp('ZYQZ', bl='加载', bc='ZKM_QvanZhongChuLiCommandsClass().ZKM_LoadText(\'textFieldButtonGrp\',\'ZYQZ\')')
        pm.button(c='ZKM_QvanZhongChuLiCommandsClass().TransferWeights()', l='转移权重(先选要转移的骨骼)')
        pm.button(c='ZKM_QvanZhongChuLiCommandsClass().ImportWeights()', l='导入权重')
        pm.setParent('..')
        pm.rowColumnLayout(bgc=(0.7, 0.7, 1), adj=2, nc=8)
        pm.textFieldGrp('ModelFace', text='2000', cw2=(80, 70), l='模型面数(大致):')
        pm.floatSliderGrp('ReduceDetail', min=1, max=100, cw3=(50, 30, 100), f=1, fieldMaxValue=9999, l='减少细节', v=20)
        pm.floatSliderGrp('Smoothness', min=1, max=100, cw3=(50, 40, 100), f=1, fieldMaxValue=9999, l='平滑程度', v=100)
        pm.setParent('..')
        pm.rowColumnLayout(bgc=(0.7, 0.7, 1), adj=1, nc=9)
        
        pm.text(l='简模镜像方向(世界轴)')
        pm.radioCollection('FKKZQSC_ModelMirror')
        pm.radioButton('None', label='None')
        pm.radioButton('X', label='X→-X')
        pm.radioButton('FX', label='-X→X')
        pm.radioButton('Y', label='Y→-Y')
        pm.radioButton('FY', label='-Y→Y')
        pm.radioButton('Z', label='Z→-Z')
        pm.radioButton('FZ', label='-Z→Z')
        pm.radioCollection('FKKZQSC_ModelMirror', edit=1, select='X')
        pm.button(c='ZKM_QvanZhongChuLiCommandsClass().GeneratingSimpleModuleApply()', l='生成简模(先清理模型)')
        
        pm.setParent('..')
        pm.setParent('..')
        pm.showWindow()
class ZKM_QvanZhongChuLiCommandsClass:
    # 加载选择为文本
    def ZKM_LoadText(self,Type,Name):
        sel=pm.ls(sl=1,fl=1)
        Sel=pm.channelBox('mainChannelBox', q=1, sma=1)
        if sel or Sel:
            #建立具体的文本
            if Sel:
                AllAttributeSel = []
                for i in range(0,len(Sel)):
                    AttributeSel=str(sel[0])+'.'+str(Sel[i])
                    AllAttributeSel.append(AttributeSel)
                AllSel=AllAttributeSel[0]
                for i in range(1,len(AllAttributeSel)):
                    AllSel=AllSel+','+AllAttributeSel[i]
            else:
                AllSel=sel[0]
                for i in range(1, len(sel)):
                    AllSel = AllSel + ',' + sel[i]
            #有属性加载物体属性，没属性加载物体
            if Sel:
                if Type == 'textFieldButtonGrp':
                    cmds.textFieldButtonGrp(Name,e=1, text=str(AllSel))
                if Type == 'textField':
                    cmds.textField(Name,e=1, text=str(AllSel))
                if Type == 'textFieldGrp':
                    cmds.textFieldGrp(Name, e=1, text=str(AllSel))
            else:
                if Type == 'textFieldButtonGrp':
                    cmds.textFieldButtonGrp(Name,e=1, text=str(AllSel))
                if Type == 'textField':
                    cmds.textField(Name,e=1, text=str(AllSel))
                if Type == 'textFieldGrp':
                    cmds.textFieldGrp(Name,e=1, text=str(AllSel))
        else:
            pm.error('请选择物体或者属性')
    # 选择对应文本的内容
    def ZKM_ReadLoadText(self,Type,Name):
        if Type == 'textFieldButtonGrp':
            Text = cmds.textFieldButtonGrp(Name, q=1, text=1)
            AllText = Text.split(',')
            pm.select(AllText)
        if Type == 'textField':
            Text = pm.select(cmds.textField(Name,q=1, text=1))
            AllText = Text.split(',')
            pm.select(AllText)
        if Type == 'textFieldGrp':
            Text = pm.select(cmds.textFieldGrp(Name,q=1, text=1))
            AllText = Text.split(',')
            pm.select(AllText)
    # 拷贝点权重
    def ZKM_CopyPointWeightApply(self):
        Soure = pm.textFieldButtonGrp('XZKBY', q=1, text=1)
        Target = pm.textFieldButtonGrp('XZKBMXHD', q=1, text=1).split(',')
        self.ZKM_CopyWeight('Normal',Soure,Target,'','')
    # 拷贝模型权重
    def ZKM_CopyModelWeightApply(self):
        AllSel = pm.ls(sl=1)
        Soure = AllSel[0]
        Target = []
        for i in range(1,len(AllSel)):
            Target.append(AllSel[i])
        self.ZKM_CopyWeight('Normal',Soure,Target,'','')
    # 对半拷贝模型权重
    def ZKM_HalfCopyModelWeightApply(self):
        AllSel = pm.ls(sl=1)
        FirstHalf = AllSel[:len(AllSel) / 2]
        LatterHalf = AllSel[len(AllSel) / 2:]
        pm.select(FirstHalf)
        pm.mel.SelectHierarchy()
        FirstHalfMesh = pm.ls(type="mesh", sl=1)
        pm.select(LatterHalf)
        pm.mel.SelectHierarchy()
        LatterHalfMesh = pm.ls(type="mesh", sl=1)
        if len(FirstHalfMesh) == len(LatterHalfMesh):
            for i in range(0, len(FirstHalfMesh)):
                pm.select(FirstHalfMesh[i], r=1)
                pm.select(LatterHalfMesh[i], add=1)
                self.ZKM_CopyModelWeightApply()
        else:
            pm.pm.mel.error("请加载偶数的选择")
    # 底层拷贝权重
    def ZKM_CopyWeight(self, CopyWay, Soure, Target, SoureUVset, TargetUVset):
        if CopyWay and Soure and Target:
            HaveWeightSoure = []
            Joint = []
            try:
                HaveWeightSoure = pm.mel.findRelatedSkinCluster(Soure)
                Joint = pm.skinCluster(Soure, q=1, inf=1)
            except:
                pass
            if len(Target[0].split('.')) == 1:
                TargetType = 'Model'
            else:
                TargetType = 'Point'
            if HaveWeightSoure:
                Removejoint = []
                # 先进行添加影响和蒙皮
                if TargetType == 'Model':
                    for T in Target:
                        try:
                            HaveWeight = pm.mel.findRelatedSkinCluster(T)
                        except:
                            HaveWeight = []
                        if HaveWeight:
                            pm.select(T)
                            pm.mel.DetachSkin()
                        pm.select(Joint, T)
                        pm.mel.SmoothBindSkin()
                if TargetType == 'Point':
                    TargetModel = Target[0].split('.')[0]
                    try:
                        HaveWeight = pm.mel.findRelatedSkinCluster(TargetModel)
                    except:
                        HaveWeight = []
                    if HaveWeight:
                        TargetJoint = pm.skinCluster(TargetModel, q=1, inf=1)
                        joint = [i for i in Joint if i not in TargetJoint]
                        if joint:
                            for j in joint:
                                pm.skinCluster(HaveWeight, e=1, ai=j, wt=0)
                        Removejoint = [i for i in TargetJoint if i not in Joint]
                        if Removejoint:
                            for j in Removejoint:
                                pm.select(Soure, j)
                                pm.skinCluster(HaveWeightSoure, e=1, ai=j, wt=0)
                    else:
                        pm.select(Joint, TargetModel)
                        pm.mel.SmoothBindSkin()
                # 进行拷贝权重
                if CopyWay == 'Normal':
                    if TargetType == 'Model':
                        for T in Target:
                            pm.select(Soure, T)
                            pm.copySkinWeights(surfaceAssociation='closestPoint',
                                               influenceAssociation=['closestJoint', 'oneToOne'], noMirror=1)
                    if TargetType == 'Point':
                        pm.select(Soure, Target)
                        pm.copySkinWeights(surfaceAssociation='closestPoint',
                                           influenceAssociation=['closestJoint', 'oneToOne'], noMirror=1)
                        if Removejoint:
                            for j in Removejoint:
                                pm.skinCluster(HaveWeightSoure, e=1, ri=j)
                if CopyWay == 'UV':
                    if SoureUVset and TargetUVset:
                        if TargetType == 'Model':
                            for T in Target:
                                pm.select(Soure, T)
                                pm.copySkinWeights(surfaceAssociation='closestPoint', uvSpace=(SoureUVset, TargetUVset),
                                                   noMirror=1, influenceAssociation=['closestJoint', 'oneToOne'])
                        if TargetType == 'Point':
                            pm.select(Soure, Target)
                            pm.copySkinWeights(surfaceAssociation='closestPoint', uvSpace=(SoureUVset, TargetUVset),
                                               noMirror=1, influenceAssociation=['closestJoint', 'oneToOne'])
                            if Removejoint:
                                for j in Removejoint:
                                    pm.skinCluster(HaveWeightSoure, e=1, ri=j)
                    else:
                        pm.error('请加载uv选集')
            else:
                pm.error('源没有骨骼蒙皮')
    # 底层平滑权重
    def ZKM_SmoothWeight(self):
        Model = pm.ls(sl=1)
        Joint = pm.skinCluster(q=1, inf=1)
        NormalizeWeight = int(pm.optionMenu('NormalizeWeight', q=1, select=1))
        pm.select(Model)
        if NormalizeWeight == 1:
            pm.skinCluster(e=1, nw=2)
        else:
            pm.skinCluster(e=1, nw=1)
        pm.select(Model)
        pm.mel.ArtPaintSkinWeightsTool()
        pm.mel.artAttrPaintOperation('artAttrSkinPaintCtx', 'Smooth')
        CS = pm.intSliderGrp('SmoothWeightType', q=1, v=1)
        for i in range(0, len(Joint)):
            pm.mel.setSmoothSkinInfluence(Joint[i])
            pm.mel.eval('artSkinRevealSelected artAttrSkinPaintCtx;')
            for J in range(0, CS):
                pm.artAttrSkinPaintCtx(pm.currentCtx(),
                                       opacity=1, clear=1, e=1)
    # 把模型分离后处理出来的权重返回整体
    def ZKM_MergeWeightsToTargetsApply(self):
        ModelGrp = pm.ls(sl=1)
        self.ZKM_ReadLoadText('textFieldButtonGrp', 'XZYMX')
        YvanModel = pm.ls(sl=1)
        self.ZKM_MergeWeightsToTargets(YvanModel,ModelGrp)
    # 把模型分离后处理出来的权重返回整体底层
    def ZKM_MergeWeightsToTargets(self,SoureModel,DecomposeModel):
        ModelCopyGrp = []
        for i in range(0, len(DecomposeModel)):
            pm.select(DecomposeModel[i])
            Joint = pm.skinCluster(q=1, inf=1)
            ModelCopy = pm.duplicate(rr=1)
            ModelCopyGrp.append(ModelCopy)
            pm.select(Joint,ModelCopy)
            pm.mel.SmoothBindSkin()
            pm.select(DecomposeModel[i], ModelCopy)
            self.ZKM_CopyModelWeightApply()
        pm.select(ModelCopyGrp)
        CureModel = pm.polyUniteSkinned(ModelCopyGrp, centerPivot=1, ch=0, mergeUVSets=1)
        pm.delete(ModelCopyGrp)
        self.ZKM_CopyWeight('Normal', CureModel[0], SoureModel, '', '')
        pm.delete(CureModel)

    #导出权重
    #ZKM_QvanZhongChuLiCommandsClass().ExportWeight(['pCube2'])
    def ExportWeight(self,Model):
        #查询当前Maya安装路径
        MAYA_VERSION = cmds.about(version=True)[:4]
        MayaPath = os.environ['HOME'] + "/maya/" + MAYA_VERSION
        #查询并建立临时文件夹
        AllPath = MayaPath.split('/')
        path = AllPath[0]
        for i in range(1,len(AllPath)):
            path = path +'\\'+ AllPath[i]
        if not os.path.exists(path+'\scripts\MayaWeightExportImportWeightProvisionalFolder'):
            os.mkdir(path+'\scripts\MayaWeightExportImportWeightProvisionalFolder')
        #清理与即将生成的文件重名的文件
        if any(name.endswith(('.xml')) for name in os.listdir(MayaPath + '/scripts/MayaWeightExportImportWeightProvisionalFolder/')):
            my_path = (MayaPath + '/scripts/MayaWeightExportImportWeightProvisionalFolder/')
            for file_name in listdir(my_path):
                if file_name.endswith('.xml'):
                    os.remove(my_path + file_name)
                if file_name.endswith('.txt'):
                    os.remove(my_path + file_name)
        #按名字创建文本
        for MD in Model:
            Joint = pm.skinCluster(MD,q=1, inf=1)
            file = open((path + '\scripts\MayaWeightExportImportWeightProvisionalFolder\\' + MD + '.txt'), "w")
            for Jon in Joint:
                file.write(Jon + '\n')
            file.close()
            SkinCluster = pm.mel.findRelatedSkinCluster(MD)
            pm.mel.eval('deformerWeights -export -deformer \"'+SkinCluster+'\" -format \"XML\" -path \"' + MayaPath + '/scripts/MayaWeightExportImportWeightProvisionalFolder/' +'\" \"'+MD+'.xml\";')
    def ExportWeights(self):
        pm.mel.RemoveUnusedInfluences()
        Model = pm.ls(sl=1)
        self.ExportWeight(Model)

    #导入权重
    #ZKM_QvanZhongChuLiCommandsClass().ImportWeight()
    # noinspection PyTypeChecker
    def ImportWeight(self,Model):
        # 查询当前Maya安装路径
        MAYA_VERSION = cmds.about(version=True)[:4]
        MayaPath = os.environ['HOME'] + "/maya/" + MAYA_VERSION
        # 查询临时文件夹
        AllPath = MayaPath.split('/')
        path = AllPath[0]
        for i in range(1, len(AllPath)):
            path = path + '\\' + AllPath[i]
        if not os.path.exists(path + '\scripts\MayaWeightExportImportWeightProvisionalFolder'):
            print('\n没有找到本插件的权重存放文件夹，请先导出权重。\n如果要查询，下面是路径：' + '\n' + str(path) + '\scripts\MayaWeightExportImportWeightProvisionalFolder\n')
        else:
            AllNodes = pm.ls(type='joint')
            for MD in Model:
                fo = open(path + "\scripts\MayaWeightExportImportWeightProvisionalFolder\\" + MD + ".txt", "r")
                lines = [l.split() for l in fo if l.strip()]
                fo.close()
                for i in range(0, len(lines)):
                    lines[i] = str(lines[i])[2:-2]
                addJoint = [x for x in lines if x not in AllNodes]  # 筛选出需要补充创建的骨骼
                for J in addJoint:  # 补充骨骼
                    pm.select(cl=1)
                    pm.joint(p=(0, 0, 0), n=J)
                try:
                    HaveSkinCluster = str(pm.mel.findRelatedSkinCluster(MD))  # 查询是否有蒙皮节点
                except:
                    HaveSkinCluster = []
                if HaveSkinCluster:
                    pm.select(MD, r=1)
                    pm.mel.DetachSkin()
                pm.select(lines, MD)
                pm.mel.SmoothBindSkin()
                pm.select(MD)
                SkinCluster = str(pm.mel.findRelatedSkinCluster(MD))  # 查询蒙皮节点
                pm.deformerWeights((MD + ".xml"),path=(MayaPath + "/scripts/MayaWeightExportImportWeightProvisionalFolder/"), im=1, method="index",deformer=SkinCluster)
                print('\n如果要查询，下面是路径：' + '\n' + str(path) + '\scripts\MayaWeightExportImportWeightProvisionalFolder\n')
    def ImportWeights(self):
        Model = pm.ls(sl=1)
        pm.mel.RemoveUnusedInfluences()
        self.ImportWeight(Model)

    def TransferWeight(self,Model):
        Joint = pm.ls(sl=1)
        SkinCluster = str(pm.mel.findRelatedSkinCluster(Model))
        pm.select((Model + ".vtx[0:999999999]"))
        pm.skinPercent(SkinCluster, tmw=[Joint[0], Joint[1]])
        pm.select(Model, r=1)
    def TransferWeights(self):
        Model = str(pm.textFieldButtonGrp('ZYQZ', q=1, text=1))
        self.TransferWeight(Model)


    def GeneratingSimpleModuleApply(self):
        ReduceDetail = float(pm.floatSliderGrp('ReduceDetail', q=1, v=1))
        Smoothness = float(pm.floatSliderGrp('Smoothness', q=1, v=1))
        ModelMirror = str(pm.radioCollection('FKKZQSC_ModelMirror', q=1, select=1))
        FaceNum = float(pm.textFieldGrp('ModelFace', q=1, text=1))
        sel = pm.ls(sl=1)
        self.GeneratingSimpleModule(sel,FaceNum, ModelMirror, ReduceDetail, Smoothness)
    def GeneratingSimpleModule(self,sel,FaceNum,ModelMirror, ReduceDetail, Smoothness):
        pm.select(sel)
        pm.duplicate(rr=1)
        sel = pm.ls(sl=1)
        if not ModelMirror == "None":
            pm.polyMirrorFace(sel[0], flipUVs=0, mirrorAxis=2, ch=0, cutMesh=1, axis=0, smoothingAngle=30,
                              mergeThresholdType=0, mergeThreshold=0.001, mergeMode=3, mirrorPosition=0,
                              axisDirection=0)
            pm.polySeparate(ch=0)
            pm.mel.DeleteHistory()
            pm.mel.CenterPivot()
            MorrySel = pm.ls(sl=1)
            Loc = pm.spaceLocator(p=(0, 0, 0))
            pm.pointConstraint(MorrySel[0], Loc, weight=1, offset=(0, 0, 0))
            num = pm.xform(Loc, q=1, ws=1, t=1)
            pm.select(MorrySel)
            if ModelMirror == "X":
                if num[0] < 0:
                    pm.delete(MorrySel[1])
                else:
                    pm.delete(MorrySel[0])
            if ModelMirror == "FX":
                if num[0] > 0:
                    pm.delete(MorrySel[1])
                else:
                    pm.delete(MorrySel[0])
            if ModelMirror == "Y":
                if num[1] < 0:
                    pm.delete(MorrySel[1])
                else:
                    pm.delete(MorrySel[0])
            if ModelMirror == "FY":
                if num[1] > 0:
                    pm.delete(MorrySel[1])
                else:
                    pm.delete(MorrySel[0])
            if ModelMirror == "Z":
                if num[2] < 0:
                    pm.delete(MorrySel[1])
                else:
                    pm.delete(MorrySel[0])
            if ModelMirror == "FZ":
                if num[2] > 0:
                    pm.delete(MorrySel[1])
                else:
                    pm.delete(MorrySel[0])
            pm.mel.DeleteHistory()
            pm.delete(Loc)
        sel = pm.ls(sl=1)
        pm.mel.polyCleanupArgList(4, ["0", "1", "1", "1", "1", "1", "1", "1", "0", "1e-05", "0", "1e-05", "0", "1e-05", "0", "2", "0", "0"])
        pm.mel.DeleteHistory()
        pm.polyRemesh(smoothStrength=Smoothness, refineThreshold=0.1, reduceThreshold=ReduceDetail,ch=0)
        pm.select(sel)
        pm.mel.DeleteHistory()
        if not ModelMirror == "None":
            FaceNum = (FaceNum / 2)
        pm.mel.polyRetopo('-targetFaceCount', FaceNum, '-targetEdgeLengthMax', 1)
        pm.mel.DeleteHistory()
        if ModelMirror == "X":
            pm.polyMirrorFace(sel[0], flipUVs=0, mirrorAxis=2, ch=1, cutMesh=1, axis=0, smoothingAngle=30,
                              mergeThresholdType=1, mergeThreshold=0.001, mergeMode=1, mirrorPosition=0,
                              axisDirection=0)

        if ModelMirror == "FX":
            pm.polyMirrorFace(sel[0], flipUVs=0, mirrorAxis=2, ch=1, cutMesh=1, axis=0, smoothingAngle=30,
                              mergeThresholdType=1, mergeThreshold=0.001, mergeMode=1, mirrorPosition=0,
                              axisDirection=1)

        if ModelMirror == "Y":
            pm.polyMirrorFace(sel[0], flipUVs=0, mirrorAxis=2, ch=1, cutMesh=1, axis=1, smoothingAngle=30,
                              mergeThresholdType=1, mergeThreshold=0.001, mergeMode=1, mirrorPosition=0,
                              axisDirection=0)

        if ModelMirror == "FY":
            pm.polyMirrorFace(sel[0], flipUVs=0, mirrorAxis=2, ch=1, cutMesh=1, axis=1, smoothingAngle=30,
                              mergeThresholdType=1, mergeThreshold=0.001, mergeMode=1, mirrorPosition=0,
                              axisDirection=1)

        if ModelMirror == "Z":
            pm.polyMirrorFace(sel[0], flipUVs=0, mirrorAxis=2, ch=1, cutMesh=1, axis=2, smoothingAngle=30,
                              mergeThresholdType=1, mergeThreshold=0.001, mergeMode=1, mirrorPosition=0,
                              axisDirection=0)

        if ModelMirror == "FZ":
            pm.polyMirrorFace(sel[0], flipUVs=0, mirrorAxis=2, ch=1, cutMesh=1, axis=2, smoothingAngle=30,
                              mergeThresholdType=1, mergeThreshold=0.001, mergeMode=1, mirrorPosition=0,
                              axisDirection=1)
        pm.mel.DeleteHistory()



'''if __name__ == '__main__':
    ZKM_QvanZhongChuLiWindowClass().ZKM_WindowQvanZhongChuLiWindow()'''
ZKM_QvanZhongChuLiWindowClass().ZKM_WindowQvanZhongChuLiWindow()