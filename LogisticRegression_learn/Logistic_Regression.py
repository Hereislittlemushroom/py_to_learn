import requests
import random

#下载IRIS数据集
data_url = "https://raw.githubusercontent.com/CrawlScript/Tensorflow-AutoEncoder/master/tutorial_datasets/iris/iris.data"
raw_data = requests.get(data_url).text

features_list = [] #用于存放所有特征
label_list = [] #用于存放所有label
label_dict = {} #字典，用于存放label名和label id的映射

last_label_id = -1
#输入label名，获取label id
#如果label_dict中已经包含了label_name，直接获取其中的label_name
#如果label_dict不包含label_name, 用当前最大的label id加1作为label id，并将其加入label_dict
def convert_label(label_name):
    global last_label_id
    if label_name in label_dict:
        return label_dict[label_name]
    else:
        last_label_id += 1
        label_dict[label_name] = last_label_id
        return last_label_id

line_list = raw_data.split() #把数据按行切分
random.shuffle(line_list) #打乱数据

#将每行数据转换为features和label
for line in line_list:
    values = line.split(",")
    features = [float(value) for value in values[:-1]] #从每行提取特征
    features_list.append(features)
    label_id = convert_label(values[-1])
    label_list.append(label_id)

total_size = len(label_list) # 计算总数据量
split_size = total_size * 4 // 5 # 取80%作训练集

#切分训练集和测试集
train_features_list = features_list[:split_size]
train_label_list = label_list[:split_size]
test_features_list = features_list[split_size:]
test_label_list = label_list[split_size:]

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(C = 1e5) #C是正则项参数的倒数，C越小正则项参数越大，正则项参数用于防止过拟合

#用训练集训练逻辑回归分类器
classifier.fit(train_features_list, train_label_list)

predict_label_list = classifier.predict(test_features_list) #分类器在测试集上预测

print("features | target | predict") #按照特征、真实label、预测label进行排版
for i in range(len(test_label_list)):
    features = test_features_list[i]
    features = [str(feature) for feature in features]
    target = test_label_list[i]
    predict = predict_label_list[i]
    print("{} | {} | {}".format(features, target, predict))
