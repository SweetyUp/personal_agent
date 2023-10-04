import json
import os

import json
import random

def split_data(jsonl_file, save_path,train_ratio=0.7, dev_ratio=0.15, test_ratio=0.15):
    # 读取JSONL文件
    data = []
    with open(jsonl_file, 'r', encoding='utf-8') as file:
        for line in file:
            record = json.loads(line)
            data.append(record)

    # 打乱数据顺序
    random.seed(1012)
    random.shuffle(data)

    # 计算数据集划分的索引
    total_count = len(data)
    train_count = int(total_count * train_ratio)
    dev_count = int(total_count * dev_ratio)

    # 划分数据集
    train_data = data[:train_count]
    dev_data = data[train_count:train_count + dev_count]
    test_data = data[train_count + dev_count:]

    for temp_train_data in train_data:
        data2jsonl( f'{save_path}train.jsonl',temp_train_data)
    for temp_dev_data in dev_data:
        data2jsonl( f'{save_path}dev.jsonl',temp_dev_data)
    for temp_test_data in test_data:
        data2jsonl(f'{save_path}test.jsonl',temp_test_data)

    return train_data, dev_data, test_data

def list_directory_structure(directory):
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}[{os.path.basename(root)}/]")
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")


def detect_language(text):
    """
    判断字符串是英文、中文还是中英混杂。
    参数：text (str): 要判断的字符串。
    返回：str: "英文"、"中文" 或 "中英混杂"。
    """
    # 初始化计数器
    chinese_count = 0
    english_count = 0

    for char in text:
        # 使用Unicode字符属性判断字符是否是汉字
        if '\u4e00' <= char <= '\u9fff':
            chinese_count += 1
        # 使用isalpha()方法判断字符是否是英文字母
        elif char.isalpha():
            english_count += 1

    # 根据计数情况判断字符串类型
    if chinese_count > 0 and english_count == 0:
        return "中文"
    elif chinese_count == 0 and english_count > 0:
        return "英文"
    else:
        return "中英混杂"

def jsonl2dict(path):
    """
    将JSON Lines文件解析为字典列表。
    参数：
    path (str): JSON Lines文件的路径。
    返回：
    list: 包含从JSON Lines文件中解析出的字典的列表。
    """
    result = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                # 使用json.loads()解析每一行，并将结果添加到列表中
                data = json.loads(line)
                result.append(data)
            except json.JSONDecodeError as e:
                print(f"解析JSON行时发生错误：{e}")
    return result

def json2dict(path):
    with open(path,'r',encoding='utf-8') as f:
        data = json.load(f)
    return data


def make_path_file(path):
    # 获取目录名和文件名
    dir_name = os.path.dirname(path)
    file_name = os.path.basename(path)
    # 如果目录不存在，创建目录
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)
    # 如果文件不存在，创建文件
    if not os.path.exists(path):
        open(path, 'w').close()


def data2jsonl(path, data, add=True):
    # 判断路径是否存在
    make_path_file(path)
    # 以追加模式或覆盖模式打开文件
    mode = 'a' if add else 'w'
    # 将数据写入JSONL文件
    with open(path, mode, encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)
        file.write('\n')


def data2json(path, response):
    # 判断路径是否存在
    make_path_file(path)
    # 数据存为json文件
    with open(path, 'w', encoding='UTF-8') as  f:
            f.write(json.dumps(response,ensure_ascii=False, indent=2))
    print('over')


def data2txt_add(path, response):
    # 判断路径是否存在
    make_path_file(path)
    # 数据存为json文件
    with open(path, 'a', encoding='UTF-8') as  f:
            f.write(response)
    print('over')


def data2txt(path, response):
    # 判断路径是否存在
    make_path_file(path)
    # 数据存为json文件
    with open(path, 'w', encoding='UTF-8') as  f:
            f.write(response)
    print('over')
