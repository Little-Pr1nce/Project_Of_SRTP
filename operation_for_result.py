from using_baidu_webapi import get_token, recognize


"""使用using_baidu_WebApi模块来完成识别过程，并且得到txt文件"""

filename = "test16k.wav"                            # 音频文件名称，必要的时候要写绝对地址
rate = 16000                                        # 音频文件的码率
form = 'wav'
signal = open(filename, "rb").read()                # 以二进制读取文件

token = get_token()
first_result = recognize(signal, rate, token, form)
print(first_result)                                 # 打印的到的语音结果


"""将得到结果，保存为txt文件，以便后续的处理"""
txt_filname = 'result_from_webapi.txt'
with open(txt_filname, 'w', encoding='utf-8') as file_object:
    """如果是a，则表示是附加模式，每一次运行都会把结果添加到文本里面"""
    """如果是w，则标示是写入模式，每一次运行都会把之前的内容删掉然后把新内容写进去"""
    file_object.write(first_result + '\n')