from using_baidu_webapi import get_token, recognize

"""使用using_baidu_WebApi模块来完成识别过程，并且得到txt文件"""

filename = "16k.wav"                                # 音频文件名称，必要的时候要写绝对地址
rate = 16000                                        # 音频文件的码率
form = 'wav'
signal = open(filename, "rb").read()                # 以二进制读取文件

token = get_token()
first_result = recognize(signal, rate, token, form)
print(first_result)                                 # 打印的到的语音结果

"""讲得到结果，保存为txt文件，以便后续的处理"""
txt_filname = 'result_from_webapi.txt'
with open(txt_filname, 'a') as file_object:
    txt = '未经纠错的语音识别文本：' + first_result + '\n'
    file_object.write(txt)
