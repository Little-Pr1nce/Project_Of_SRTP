import pypinyin
import operation_for_vocabularylib

"""把初始的结果进行纠错"""

"""首先读取test2.xls文件的内容，然后转化为字典来进一步处理"""
vocabulary_filename = "/Users/little-prince/Documents/语言处理/test2.xls"  # 包含拼音的单词库的绝对路径
result = operation_for_vocabularylib.read_xls_file_return(vocabulary_filename)
result_dic = dict(result)  # 把得到的列表字典化
#  {'拼音': '症状名',
# 'zheng-zhuang-ci': '症状词',
# 'ji-zao-yi-nu': '急躁易怒',
# 'ao-nong-nan-ming': '懊侬难名',
# 'ao-nong-nan-zhuang': '懊侬难状',
# 'qi-si-wo-le': '气死我了',
# 'luo-pang': '罗胖'}

"""先开始进行最简单的单词纠错"""

"""开始单词的纠错，example为熬浓南明-->懊侬难名"""
untreated_filename = "result_from_webapi.txt"  # 这就是从调用语音识别api得到的没有改错过的文本的路径
with open(untreated_filename, 'r+', encoding='utf-8') as file_object:
    """读取文件"""
    txt = file_object.read()


def correct_for_word(fil):
    """通过输入的字符串文件，来进行单词方面的纠错"""
    txt_py = pypinyin.slug(fil, errors='ignore')
    for key in result_dic.keys():
        if key == txt_py:
            fil = result_dic[key]
    return fil


result = correct_for_word(txt)
print(result)

"""把修改的结果放到result_final文件，这就是纠错之后的文本"""
treated_filename = "result_final.txt"  # 最终纠错后的文本的路径
with open(treated_filename, "w", encoding='utf-8') as file_object:
    txt1 = correct_for_word(result)
    file_object.write(txt1)

