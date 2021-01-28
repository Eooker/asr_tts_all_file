# coding=utf-8
import re
import json
import urllib
import urllib.request

#彩色输出函数
def color_print (color,text):          #参数：color 字体颜色 text 输出文本   颜色编号：0黑色 1红色 2绿色 3棕色 4蓝色 5紫色 6青色 7白色
	color=str(color+30)
	print("\033[1;"+color+"m"+text+"\033[0m")

with open('/home/pi/my_ASR_TTS/process/asr_result.txt','r') as asr_result_file:      #打开语音识别的结果文本
    text=asr_result_file.read()    #获取文本内容
text=urllib.parse.quote(text)       #将文本内容转换成适合于网络传输的形式
url="http://api.qingyunke.com/api.php?key=free&appid=0&msg=%s"%(text)   #形成请求地址
try:
    receive_data=urllib.request.urlopen(url)     #发送请求并接收返回数据
    
    data=receive_data.read()          #提取返回数据内容
    data_str=str(data,'utf-8')     #将提取内容转换为中文
    data_dict=json.loads(data_str)      #将提取内容恢复为python数据类型：字典
    if data_dict['result'] == 0 :   #判断是否返回正确数据
        color_print(7,"成功收到回信！")
        with open("/home/pi/my_ASR_TTS/process/chat_result.txt","w") as result_file:
            result_file.write(data_dict['content'])
    else:    #返回数据错误，将错误提示写进error.txt
        with open("/home/pi/my_ASR_TTS/error/error.txt","w") as error_file:
            error_file.write("聊天数据错误。")
except:
    with open("/home/pi/my_ASR_TTS/error/error.txt","w") as error_file:
        error_file.write("聊天请求失败。")
