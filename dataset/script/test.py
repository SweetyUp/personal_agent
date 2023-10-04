from data_tools import *

jsonl_file = r'./dataset/pro_dataset/data_1004/Haruhi_50K_v1.jsonl'
output_train_file = r'./dataset/pro_dataset/data_1004/train.jsonl'
output_dev_file = r'./dataset/pro_dataset/data_1004/dev.jsonl'
output_test_file = r'./dataset/pro_dataset/data_1004/test.jsonl'
save_path = r'./dataset/pro_dataset/data_1004/'
train_data, val_data, test_data = split_data(jsonl_file,save_path=save_path, train_ratio=0.98, dev_ratio=0.15, test_ratio=0.05)
print(len(train_data), len(val_data), len(test_data))
print(type(train_data), type(val_data), type(test_data))
print(test_data[0])
