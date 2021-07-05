# -*- coding: utf-8 -*-
import os
import time
import json
import cv2
 
 
xml_head = '''<annotation>
    <folder>traffic-sign</folder>
    <!--文件名-->
    <filename>{}</filename>  
    <size>
        <width>2048</width>
        <height>2048</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>
    <category>{}</category>
    '''
xml_obj = '''
    <object>     
        <!--图片中目标类别-->   
        <name>{}</name>
        <!--是否被裁减，0表示完整，1表示不完整-->
        <truncated>0</truncated>
        <!--是否容易识别，0表示容易，1表示困难-->
        <difficult>0</difficult>
        <bndbox>
            <xmin>{}</xmin>
            <ymin>{}</ymin>
            <xmax>{}</xmax>
            <ymax>{}</ymax>
        </bndbox>
    </object>
    '''
xml_end = '''
</annotation>'''
anno = 'D:\Shaoooooo/tt100k_2021/tt100k_2021/annotations_all.json'# json文件路径
xml_dir = 'D:\Shaoooooo/tt100k_2021/tt100k_2021/newxml'#存放xml文件的路径
labels = ['w1','w2','w3','w4','w5','w6','w7','w8','w9','w10','w11','w12','w13','w14','w15'\
            ,'w16'\
,'w17'\
,'w18'\
,'w19'\
,'w20'\
,'w21'\
,'w22'\
,'w23'\
,'w24'\
,'w25'\
,'w26'\
,'w27'\
,'w28'\
,'w29'\
,'w30'\
,'w31'\
,'w32'\
,'w33'\
,'w34'\
,'w35'\
,'w36'\
,'w37'\
,'w38'\
,'w39'\
,'w40'\
,'w41'\
,'w42'\
,'w43'\
,'w44'\
,'w45'\
,'w46'\
,'w47'\
,'w48'\
,'w49'\
,'w50'\
,'w51'\
,'w52'\
,'w53'\
,'w54'\
,'w55'\
,'w56'\
,'w57'\
,'w58'\
,'w59'\
,'w60'\
,'w61'\
,'w62'\
,'w63'\
,'w64'\
,'w65'\
,'w66'\
,'w67'\
,'p1'\
,'p2'\
,'p3'\
,'p4'\
,'p5'\
,'p6'\
,'p7'\
,'p8'\
,'p9'\
,'p10'\
,'p11'\
,'p12'\
,'p13'\
,'p14'\
,'p15'\
,'p16'\
,'p17'\
,'p18'\
,'p19'\
,'p20'\
,'p21'\
,'p22'\
,'p23'\
,'p24'\
,'p25'\
,'p26'\
,'p27'\
,'p28'\
,'pd','pn','pnl','ps','pg','pb','pe','pne'\
,'i1'\
,'i2'\
,'i3'\
,'i4'\
,'i5'\
,'i6'\
,'i7'\
,'i8'\
,'i9'\
,'i10'\
,'i11'\
,'i12'\
,'i13'\
,'i14'\
,'i15'\
,'ip','pm1.5','ph48','pm35','pm8','pa14','ph5','pa13','pl100'\
,'ph2.1','ph3.5','pr50','pm30','pm20','pl110','pl65','ph2.2',\
'pm5','ph4.3','pm2.5','pm46','pl50','pl10','ph3.2','p8','il60',\
'ph3.3','ph4.5','pl30','il110','pa12','il70','pa8','ph2.9',\
'pm15','ph1.8','pm55','pr100','pm50','pl20','ph2.8','pl60','pw4',\
'pm40','ph2.4','pl120','il50','pa6','il100','il80','ph4.4','pm2','ph4.2','pa10',\
'pl90','pr5','pm25','pa18','pr30','pw4.2','ph2.6','pl80','pw3','pl70'\
,'pl15','pr40','pr10','pw2.5','pl5','pm13','pr70','pr60','pw4.5','il90','ph3.8','pl40','ph2.5','ph3','ph5.5','ph5.3','ph2','pl25','pl35','pm10','pr80',\
'pr45','ph4','pw3.5','pw3.2','pr20','pw*','pl*']  # label for datasets
print("labels类型：",type(labels))
# 读取json文件内容,返回字典格式
with open(anno,'r',encoding='utf8')as fp:
    json_data = json.load(fp)
    #imgs数据，字典类型
    json_imgs=json_data['imgs']
    #记录小目标总数目,共2908
    count=0
    count_w1=0
    count_w2=0
    count_w3=0
    count_w4=0
    count_w5=0
    count_w6=0
    count_w7=0
    count_w8=0
    count_w9=0
    count_w10=0
    count_w11=0
    count_w12=0
    count_w13=0
    count_w14=0
    count_w15=0
    count_w16=0
    count_w17=0
    count_w18=0
    count_w19=0
    count_w20=0
    count_w21=0
    count_w22=0
    count_w23=0
    count_w24=0
    count_w25=0
    count_w26=0
    count_w27=0
    count_w28=0
    count_w29=0
    count_w30=0
    count_w31=0
    count_w32=0
    count_w33=0
    count_w34=0
    count_w35=0
    count_w36=0
    count_w37=0
    count_w38=0
    count_w39=0
    count_w40=0
    count_w41=0
    count_w42=0
    count_w43=0
    count_w44=0
    count_w45=0
    count_w46=0
    count_w47=0
    count_w48=0
    count_w49=0
    count_w50=0
    count_w51=0
    count_w52=0
    count_w53=0
    count_w54=0
    count_w55=0   
    count_w56=0
    count_w57=0
    count_w58=0
    count_w59=0
    count_w60=0
    count_w61=0
    count_w62=0
    count_w63=0
    count_w64=0
    count_w65=0   
    count_w66=0
    count_w67=0
    count_p1=0
    count_p2=0
    count_p3=0
    count_p4=0
    count_p5=0
    count_p6=0
    count_p7=0
    count_p8=0
    count_p9=0
    count_p10=0
    count_p11=0
    count_p12=0
    count_p13=0
    count_p14=0
    count_p15=0
    count_p16=0
    count_p17=0
    count_p18=0
    count_p19=0
    count_p20=0
    count_p21=0
    count_p22=0
    count_p23=0
    count_p24=0
    count_p25=0
    count_p26=0
    count_p27=0
    count_p28=0
    count_pd=0
    count_pn=0
    count_pnl=0
    count_ps=0
    count_pg=0
    count_pb=0
    count_pe=0
    count_pne=0
    count_i1=0
    count_i2=0
    count_i3=0
    count_i4=0
    count_i5=0
    count_i6=0
    count_i7=0
    count_i8=0
    count_i9=0
    count_i10=0
    count_i11=0
    count_i12=0
    count_i13=0
    count_i14=0
    count_i15=0
    count_ip=0
    #count_pne_trian训练文件夹中pne数量
    count_pne_trian=0
    # count_p11_trian训练文件夹中p11数量
    count_p11_trian = 0
    # count_i5_trian训练文件夹中i5数量
    count_i5_trian = 0
    # count_w57_trian训练文件夹中w57数量
    count_w57_trian = 0
    #训练pne数量
    count_img_pne_train=0
    #训练p11数量
    count_img_p11_train=0
    #训练i5数量
    count_img_i5_train=0
    #训练w57数量
    count_img_w57_train=0
    # 测试pne数量
    count_img_pne_test=0
    # 测试p11数量
    count_img_p11_test=0
    # 测试i5数量
    count_img_i5_test=0
    # 测试w57数量
    count_img_w57_test=0
 
    #图片总数
    count_image=0;
    dict = {'w1','w2','w3','w4','w5','w6','w7','w8','w9','w10','w11','w12','w13','w14','w15'\
            ,'w16'\
,'w17'\
,'w18'\
,'w19'\
,'w20'\
,'w21'\
,'w22'\
,'w23'\
,'w24'\
,'w25'\
,'w26'\
,'w27'\
,'w28'\
,'w29'\
,'w30'\
,'w31'\
,'w32'\
,'w33'\
,'w34'\
,'w35'\
,'w36'\
,'w37'\
,'w38'\
,'w39'\
,'w40'\
,'w41'\
,'w42'\
,'w43'\
,'w44'\
,'w45'\
,'w46'\
,'w47'\
,'w48'\
,'w49'\
,'w50'\
,'w51'\
,'w52'\
,'w53'\
,'w54'\
,'w55'\
,'w56'\
,'w57'\
,'w58'\
,'w59'\
,'w60'\
,'w61'\
,'w62'\
,'w63'\
,'w64'\
,'w65'\
,'w66'\
,'w67'\
,'p1'\
,'p2'\
,'p3'\
,'p4'\
,'p5'\
,'p6'\
,'p7'\
,'p8'\
,'p9'\
,'p10'\
,'p11'\
,'p12'\
,'p13'\
,'p14'\
,'p15'\
,'p16'\
,'p17'\
,'p18'\
,'p19'\
,'p20'\
,'p21'\
,'p22'\
,'p23'\
,'p24'\
,'p25'\
,'p26'\
,'p27'\
,'p28'\
,'pd','pn','pnl','ps','pg','pb','pe','pne'\
,'i1'\
,'i2'\
,'i3'\
,'i4'\
,'i5'\
,'i6'\
,'i7'\
,'i8'\
,'i9'\
,'i10'\
,'i11'\
,'i12'\
,'i13'\
,'i14'\
,'i15'\
,'ip'}
    table=['pne']
    for item in json_imgs.items():
        #item是tuple类型 ,item元组中共有两个元素，一开始的ID和图片详细信息
        #detail_info为图片详细信息，是字典类型，含有path，objects，id三个key值
        detail_info=item[1]
        #path图片路径
        image_path=detail_info['path']
        if image_path.find('train')!=-1 or image_path.find('test')!=-1:
            #图片含有的目标,list类型
            image_objects=detail_info['objects']
            # 图片的id
            image_id = detail_info['id']
            # flag_category记录category的标记
            flag_category = ''
            #obj表示一个图片中目标信息
            obj=''
            for info in range(len(image_objects)):
                # object_info是object的详细信息,数据类型为字典，包含category，objects
                object_info = image_objects[info]
                #object_category是object的category,字符串
                object_category = object_info['category']
                # object_bbox为字典类型，存放目标信息xmin,ymin,xmax,ymax
                object_bbox = object_info['bbox']
                #x_rang目标的x间的大小，xmax-xmin
                x_rang=object_bbox['xmax']-object_bbox['xmin']
                #目标的y间的大小，ymax-ymin
                y_rang=object_bbox['ymax']-object_bbox['ymin']
                #flag=0
                if x_rang <= 32 and y_rang <= 32:
                    for oui in dict:
                        if object_category == oui:
                            if flag_category == '':
                                flag_category = object_category
                            obj+=xml_obj.format(labels[0],str(object_bbox['xmin']),str(object_bbox['ymin']),
                                            str(object_bbox['xmax']),str(object_bbox['ymax']))

            #表示有合适类别的小目标的时候开始创建xml文件,存放在了test和train文件夹下面
            if flag_category!='' :
                if image_path.find('train') != -1:
                    for item in dict:
                        if flag_category==item:
                            count_img_pne_train+=1
                            xml_name = os.path.join(xml_dir + '/trains/'+item+'/', str(image_id) + '.xml')
                else :
                    for item in dict:
                        if flag_category==item:
                            continue
                            xml_name = os.path.join(xml_dir + '/tests/'+item+'/', str(image_id) + '.xml')
                print("xml_name:"+xml_name)
                print("image_id:",image_id)
                #xml的头部信息传入参数值，文件名字和类别
                head=xml_head.format(str(xml_name),str(flag_category))
                #xml的尾部信息
                end=xml_end
                #向xml文件中写入内容
                with open(xml_name, 'w') as f:
                    f.write(head+obj+end)

