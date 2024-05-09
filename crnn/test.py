import torch

try:
    # 替换为您的实际模型文件路径
    model = torch.load('saved_model/1.pth')
    print("模型加载成功！")
except Exception as e:
    print("加载模型时出错：", e)

import torch

# 使用 map_location 将所有张量映射到 CPU
model_path = 'saved_model/1.pth'
model = torch.load(model_path, map_location=torch.device('cpu'))

print("模型已成功加载到 CPU。")
