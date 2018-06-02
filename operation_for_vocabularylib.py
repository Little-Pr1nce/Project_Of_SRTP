from collections import OrderedDict
from pyexcel_xls import save_data
from pyexcel_xls import get_data
import pypinyin

"""处理单词库，添加拼音进入单词库"""
"""查看资料网址：https://www.cnblogs.com/alfred0311/p/7809863.html"""

"""pyexcel_xls 以 OrderedDict 结构处理数据"""


def read_xls_file_print(fil):
    """读取xls文件,并打印出结果  """
    """fil为读取文件的绝对路径"""
    data = get_data(fil)
    print("数据格式：", type(data))
    for sheet_n in data.keys():
        print(sheet_n, ":", data[sheet_n])


def read_xls_file_return(fil):
    """读取xls文件,并返回出结果"""
    """fil为读取文件的绝对路径"""
    data = get_data(fil)
    for sheet_n in data.keys():
        return data[sheet_n]


def str_of_result(res):
    """把得到的列表文件中的元素从列表转化到字符串，并处理字符串可以直接被pinyin模块识别"""
    """参数res就是读取xls文件得到的那个列表，是read_xls_file两个函数的返回结果"""
    row = []
    for value in range(0, len(res)):
        no1     = res[value]
        no11    = str(no1)
        last_no = no11[2:len(no11) - 2]
        row.append(last_no)
    return row


def addition_pinyin(data, num):
    """得到一个有症状名和对应拼音的列表,返回这个列表"""
    """data参数是str_of_result函数处理后的列表，num是处理后列表的长度"""
    row = []  # 新建一个空列表
    for value in range(0, num):
        py  = pypinyin.slug(data[value])  # 每个词的拼音
        tem = [data[value], py]
        row.append(tem)
    return row


def save_xls_file(res, fil):
    """把处理后的列表保存在xls格式文件里面"""
    """res就是addition_pinyin函数处理后的列表，fil就是xls文件的绝对地址"""
    data = OrderedDict()
    # sheet表数据
    sheet_1    = []  # 首先把sheet置空
    row_1_data = ['拼音', '症状名']  # 第一行的数据
    sheet_1.append(row_1_data)
    # 逐行添加症状名和数据
    for value in range(0, len(res)):
        initial = res[value]
        symptom = initial[0]
        py      = initial[1]
        row_value_data = [py, symptom]
        sheet_1.append(row_value_data)
    # 添加sheet表
    data.update({"sheet1": sheet_1})
    # 保存为xls文件
    save_data(fil, data)