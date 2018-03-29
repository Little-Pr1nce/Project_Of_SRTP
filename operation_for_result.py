from using_baidu_webapi import get_token, recognize

"""使用using_baidu_WebApi模块来完成识别过程，并且得到txt文件"""

filename = "16k.wav"                                # 音频文件名称，必要的时候要写绝对地址
rate = 16000                                        # 音频文件的码率
form = 'wav'
signal = open(filename, "rb").read()                # 读取文件

token = get_token()
first_result = recognize(signal, rate, token, form)
print(first_result)
