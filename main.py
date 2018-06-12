from using_baidu_webapi import get_token, recognize
from methods_for_correction import save_file, read_file
from operation_for_vocabularylib import read_xls_file_return, str_of_result, addition_pinyin, save_xls_file
from methods_for_correction import correct_txt_with_info

"""基于领域文本的自动纠错系统后端的主函数 by michael"""

"""1）首先使用using_baidu_WebApi模块来完成识别过程，并且得到txt文件"""

voice_filename = "测试音频2/新录音 14.wav"            # 音频文件名称，必要的时候要写绝对地址
uncorrected_txt_filename = "/Users/little-prince/Documents/语言处理/result_from_webapi.txt"  # 没有纠错的文本的文件路径
rate = 16000                                # 音频文件的码率
form = 'wav'                                # 音频文件的格式

signal = open(voice_filename, "rb").read()  # 以二进制读取文件
token = get_token()                         # 获取网页的token
first_result = recognize(signal, rate, token, form)  # 得到网页翻译的结果
print('网页识别的结果为：' + first_result)                                  # 打印的到的语音结果
save_file(uncorrected_txt_filename, first_result)

"""2）将保存的网页识别的结果进行纠错"""

"""2.1）首先，对给定的领域文本库进行处理，方便后续纠错的使用"""
source_filname     = '/Users/little-prince/Documents/语言处理/症状实验.xls'  # 原始库文件的绝对地址
vocabulary_filname = '/Users/little-prince/Documents/语言处理/pinyin_for_lib.xls'  # 可供比对的单词库

result_1 = read_xls_file_return(source_filname)
result_2 = str_of_result(result_1)
result_3 = addition_pinyin(result_2, len(result_2))
save_xls_file(result_3, vocabulary_filname)  # 保存生成的可供对比的单词库

"""2.2)开始纠错"""

"""2.2.1)首先读取pinyin_for_lib库的文件的内容，然后转化为字典来进一步处理"""
py = read_xls_file_return(vocabulary_filname)  # 读取可供对比的单词库内容
py_dic = dict(py)                              # 把得到的列表字典化

"""2.2.2)开始进行文本纠错"""
uncorrected_txt_filename = "/Users/little-prince/Documents/语言处理/result_from_webapi.txt"  # 没有纠错的文本的文件路径
final_filname = "/Users/little-prince/Documents/语言处理/result_final.txt"                   # 纠错后文本的文件路径
uncorrected_txt = read_file(uncorrected_txt_filename)
final_txt = correct_txt_with_info(uncorrected_txt, py_dic)
print('纠错后的结果为：' + final_txt['text'])
print('涉及到的领域词汇个数为: ' + str(final_txt['num']))
print('这些领域词汇有：' + str(final_txt['word']))

"""2.2.3)保存纠错的结果"""
result_dic = {'纠错后的结果为：': final_txt['text'],
              '涉及到的领域词汇个数为: ': str(final_txt['num']),
              '这些领域词汇有：': str(final_txt['word'])}
txt = ''
for key, value in result_dic.items():
    txt = txt + key + value + '\n'
save_file(final_filname, txt)
