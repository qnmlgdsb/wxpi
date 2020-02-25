import json,requests,os #调用模块，后期运行命令调用os
url = requests.get('http://192.168.11.27/json') #获取地址http://10.0.0.27/json
wd = json.loads(url.text) #载入字典准备查询
wendu = int(wd['Sensors'][0]['TaskValues'][0]['Value']) #找到温度所在字符串位置
xwendu = str(wendu)
wxbj = 'https://url/weixin.php?msg='+'现在服务器机房'+xwendu+'度'
wxerr = 'https://url/weixin.php?msg='+'现在程序有问题'
if wendu >=24: #判断并且显示温度高低，后期修改为os运行命令
	print('Hot Temp is:',wendu,'°C')
	#bulb.turn_on()
	#bulb1.turn_on()
	#bulb.set_rgb(243, 9, 15)
	#bulb1.set_rgb(198, 135, 15)
	requests.post(wxbj)
elif wendu <24:
	print('Hot Temp is:',wendu,'°C')
	#bulb.turn_off()
	#bulb.set_rgb(0, 225,233)
else:
  print('Cool Temp is:',wendu,'°C')
  #bulb.turn_off()
  requests.post(wxerr)
