import pypinyin
import pytrie

"""把初始的结果进行纠错"""


def read_file(fil):
    """
    把txt文件中的字符串读取出来
    :param fil: 文件的相对路径
    :return: 字符串
    """
    with open(fil, 'r+', encoding='utf-8') as file_object:
        """读取文件"""
        txt = file_object.read()
        return txt


def save_file(fil, txt):
    """

    :param fil: 要保存的文件路径
    :param txt: 要保存的文件
    :return: 没有return，如果保存错误返回error
    """
    with open(fil, 'w', encoding='utf-8') as file_object:
        file_object.write(txt)


def correct_for_word(fil, dic):
    """
    用来纠错单个单词的
    :param fil:输入一个单词
    :param dic:字典化的标准单词库
    :return:返回一个纠错好的单词
    """
    txt_py = pypinyin.slug(fil, errors='ignore')
    for key in dic.keys():
        if key == txt_py:
            fil = dic[key]
    return fil


def correct_for_txt(txt, dic):
    """
    修改文章中需要纠错的单词
    :param txt: 需要纠错的文本
    :param dic: 已经字典化的包含拼音的标准文本库
    :return: 纠错完成的句子
    """
    num = len(txt)  # 文本的长度
    txt1 = txt  # 得到文本的副本
    vocabulary_trie = pytrie.SortedStringTrie(dic)  # 生成拼音字典的匹配trie

    for value in range(0, num):
        tem_txt = txt[value:num]  # 得到子串
        tem_py = pypinyin.slug(tem_txt)  # 子串的拼音
        """开始处理子串,把子串作为参数，进行匹配"""
        result_match = vocabulary_trie.longest_prefix_value(tem_py, default='false')
        if result_match == 'false':
            continue
        else:
            need_change = tem_txt[0:len(result_match)]  # 需要被纠错的单词
            txt1 = txt1.replace(need_change, result_match)

    return txt1  # 返回纠错过的正确文本
