# from plateNet import myNet_ocr
# import torch
# import torch.nn as nn
# import cv2
# import numpy as np
# import os
# import time
# import argparse
# from alphabets import plate_chr
# from LPRNet import build_lprnet
#
#
#
# def cv_imread(path):   #读取中文路径的图片
#     img=cv2.imdecode(np.fromfile(path,dtype=np.uint8),-1)
#     return img
#
# def allFilePath(rootPath,allFIleList):
#     fileList = os.listdir(rootPath)
#     for temp in fileList:
#         if os.path.isfile(os.path.join(rootPath,temp)):
#             allFIleList.append(os.path.join(rootPath,temp))
#         else:
#             allFilePath(os.path.join(rootPath,temp),allFIleList)
#
# mean_value,std_value=(0.588,0.193)
# def decodePlate(preds):
#     pre=0
#     newPreds=[]
#     for i in range(len(preds)):
#         if preds[i]!=0 and preds[i]!=pre:
#             newPreds.append(preds[i])
#         pre=preds[i]
#     return newPreds
#
# def image_processing(img,device,img_size):
#     img_h,img_w= img_size
#     img = cv2.resize(img, (img_w,img_h))
#     # img = np.reshape(img, (48, 168, 3))
#
#     # normalize
#     img = img.astype(np.float32)
#     img = (img / 255. - mean_value) / std_value
#     img = img.transpose([2, 0, 1])
#     img = torch.from_numpy(img)
#
#     img = img.to(device)
#     img = img.view(1, *img.size())
#     return img
#
# def get_plate_result(img,device,model,img_size):
#     # img = cv2.imread(image_path)
#     input = image_processing(img,device,img_size)
#     preds = model(input)
#     preds =preds.argmax(dim=2)
#     # print(preds)
#     preds=preds.view(-1).detach().cpu().numpy()
#     newPreds=decodePlate(preds)
#     plate=""
#     for i in newPreds:
#         plate+=plate_chr[int(i)]
#     return plate
#
# def init_model(device,model_path):
#     check_point = torch.load(model_path,map_location=device)
#     model_state=check_point['state_dict']
#     cfg = check_point['cfg']
#     model = myNet_ocr(num_classes=len(plate_chr),export=True,cfg=cfg)        #export  True 用来推理
#     # model =build_lprnet(num_classes=len(plate_chr),export=True)
#     model.load_state_dict(model_state)
#     model.to(device)
#     model.eval()
#     return model
#
# # 在 demo.py 中添加这个函数
# def get_plate_result_from_path(image_path, device):
#     img = cv_imread(image_path)
#     if img.shape[-1] != 3:
#         img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
#     plate = get_plate_result(img, device, model, img_size)
#     return plate
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--model_path', type=str, default='saved_model/1.pth', help='model.pt path(s)')
#     # parser.add_argument('--image_path', type=str, default='images/tmp6FC6.png', help='source')
#     parser.add_argument('--image_path', type=str, default='new/02D41166_1.jpg', help='source')
#     # parser.add_argument('--image_path', type=str, default='/mnt/Gu/trainData/plate/new_git_train/val_verify', help='source')
#     parser.add_argument('--img_h', type=int, default=48, help='height')
#     parser.add_argument('--img_w',type=int,default=168,help='width')
#     parser.add_argument('--LPRNet',action='store_true',help='use LPRNet')  #True代表使用LPRNet ,False代表用plateNet
#     parser.add_argument('--acc',type=bool,default='True',help=' get accuracy')  #标记好的图片，计算准确率
#     device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#     # device =torch.device("cpu")
#     opt = parser.parse_args()
#     img_size = (opt.img_h,opt.img_w)
#     model = init_model(device,opt.model_path)
#     if os.path.isfile(opt.image_path):   #判断是单张图片还是目录
#         right=0
#         begin = time.time()
#         img = cv_imread(opt.image_path)
#         if img.shape[-1]!=3:
#             img = cv2.cvtColor(img,cv2.COLOR_BGRA2BGR)
#         plate=get_plate_result(img, device,model,img_size)
#         print(plate)
#     elif opt.acc:
#         file_list=[]
#         right=0
#         allFilePath(opt.image_path,file_list)
#         for pic_ in file_list:
#             # try:
#                 pic_name = os.path.basename(pic_)
#                 img = cv_imread(pic_)
#                 if img.shape[-1]!=3:
#                     img = cv2.cvtColor(img,cv2.COLOR_BGRA2BGR)
#                 plate=get_plate_result(img,device,model,img_size)
#                 plate_ori = pic_.split('/')[-1].split('_')[0]
#         # print(plate,"---",plate_ori)
#                 if(plate==plate_ori):
#
#                     right+=1
#                 else:
#                     print(plate_ori,"rec as ---> ",plate,pic_)
#                     # print(plate,pic_name)
#             # except:
#             #         print("error")
#         print("sum:%d ,right:%d , accuracy: %f"%(len(file_list),right,right/len(file_list)))
#     else:
#             file_list=[]
#             allFilePath(opt.image_path,file_list)
#             for pic_ in file_list:
#                 try:
#                     pic_name = os.path.basename(pic_)
#                     img = cv_imread(pic_)
#                     if img.shape[-1]!=3:
#                         img = cv2.cvtColor(img,cv2.COLOR_BGRA2BGR)
#                     plate=get_plate_result(img,device,model)
#                     print(plate,pic_name)
#                 except:
#                     print("error")
#
#
#
import argparse
import torch
import cv2
import numpy as np
import os
from crnn.plateNet import myNet_ocr
from crnn.alphabets import plate_chr
#这里为了配合服务器使用以下第一行路径，如果拉下来想自己本地运行请改成自己电脑的本地路径，下面两个同理
#def init_model(device, model_path='/home/student/jialin/crnn/saved_model/1.pth'):
def init_model(device, model_path='C:/Users/tianj/PycharmProjects/COMP3030J_Group_10_J0303/crnn/saved_model/1.pth'):
    check_point = torch.load(model_path, map_location=device)
    model_state = check_point['state_dict']
    cfg = check_point['cfg']
    model = myNet_ocr(num_classes=len(plate_chr), export=True, cfg=cfg)
    model.load_state_dict(model_state)
    model.to(device)
    model.eval()
    return model


# def init_model(device):
#     model_path = 'saved_model/1.pth'
#     check_point = torch.load(model_path, map_location=device)
#     model_state = check_point['state_dict']
#     cfg = check_point['cfg']
#     model = myNet_ocr(num_classes=len(plate_chr), export=True, cfg=cfg)
#     model.load_state_dict(model_state)
#     model.to(device)
#     model.eval()
#     return model

parser = argparse.ArgumentParser()
#parser.add_argument('--model_path', type=str, default='/home/student/jialin/crnn/saved_model/1.pth', help='model.pt path(s)')
parser.add_argument('--model_path', type=str, default='C:/Users/tianj/PycharmProjects/COMP3030J_Group_10_J0303/crnn/saved_model/1.pth', help='model.pt path(s)')
# parser.add_argument('--image_path', type=str, default='images/tmp6FC6.png', help='source')
#parser.add_argument('--image_path', type=str, default='/home/student/jialin/crnn/new/02D41166_1.jpg', help='source')
parser.add_argument('--image_path', type=str, default='C:/Users/tianj/PycharmProjects/COMP3030J_Group_10_J0303/crnn/new/02D41166_1.jpg', help='source')
# parser.add_argument('--image_path', type=str, default='/mnt/Gu/trainData/plate/new_git_train/val_verify', help='source')
parser.add_argument('--img_h', type=int, default=48, help='height')
parser.add_argument('--img_w',type=int,default=168,help='width')
parser.add_argument('--LPRNet',action='store_true',help='use LPRNet')  #True代表使用LPRNet ,False代表用plateNet
parser.add_argument('--acc',type=bool,default='True',help=' get accuracy')  #标记好的图片，计算准确率
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# device =torch.device("cpu")
opt, unknown = parser.parse_known_args()
img_size = (opt.img_h,opt.img_w)
model = init_model(device,opt.model_path)


def cv_imread(path):
    img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)
    return img

def get_plate_result(img, device, model, img_size):
    img = cv2.resize(img, (img_size[1], img_size[0]))
    img = img.astype(np.float32)
    img = (img / 255.0 - 0.588) / 0.193
    img = img.transpose([2, 0, 1])
    img = torch.from_numpy(img)
    img = img.to(device)
    img = img.unsqueeze(0)
    preds = model(img)
    preds = preds.argmax(dim=2)
    preds = preds.view(-1).cpu().numpy()

    # Decode plate
    last_label = 0
    output_label = []
    for label in preds:
        if label != last_label:
            output_label.append(label)
            last_label = label
    plate = ''.join([plate_chr[label] for label in output_label if label != 0])
    return plate



device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = init_model(device)

def recognize_plate(image_path):
    img = cv_imread(image_path)
    if img.shape[-1] != 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    plate = get_plate_result(img, device, model, (48, 168))
    return plate

def cv_imread(path):   #读取中文路径的图片
    img=cv2.imdecode(np.fromfile(path,dtype=np.uint8),-1)
    return img

def allFilePath(rootPath,allFIleList):
    fileList = os.listdir(rootPath)
    for temp in fileList:
        if os.path.isfile(os.path.join(rootPath,temp)):
            allFIleList.append(os.path.join(rootPath,temp))
        else:
            allFilePath(os.path.join(rootPath,temp),allFIleList)

mean_value,std_value=(0.588,0.193)
def decodePlate(preds):
    pre=0
    newPreds=[]
    for i in range(len(preds)):
        if preds[i]!=0 and preds[i]!=pre:
            newPreds.append(preds[i])
        pre=preds[i]
    return newPreds

def image_processing(img,device,img_size):
    img_h,img_w= img_size
    img = cv2.resize(img, (img_w,img_h))
    # img = np.reshape(img, (48, 168, 3))

    # normalize
    img = img.astype(np.float32)
    img = (img / 255. - mean_value) / std_value
    img = img.transpose([2, 0, 1])
    img = torch.from_numpy(img)

    img = img.to(device)
    img = img.view(1, *img.size())
    return img

def get_plate_result(img,device,model,img_size):
    # img = cv2.imread(image_path)
    input = image_processing(img,device,img_size)
    preds = model(input)
    preds =preds.argmax(dim=2)
    # print(preds)
    preds=preds.view(-1).detach().cpu().numpy()
    newPreds=decodePlate(preds)
    plate=""
    for i in newPreds:
        plate+=plate_chr[int(i)]
    return plate

def init_model(device,model_path):
    check_point = torch.load(model_path,map_location=device)
    model_state=check_point['state_dict']
    cfg = check_point['cfg']
    model = myNet_ocr(num_classes=len(plate_chr),export=True,cfg=cfg)        #export  True 用来推理
    # model =build_lprnet(num_classes=len(plate_chr),export=True)
    model.load_state_dict(model_state)
    model.to(device)
    model.eval()
    return model

