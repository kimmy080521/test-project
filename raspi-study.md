## 学习资料
### 1、摩尔吧视视频教程
https://www.moore8.com/courses/video/1992/26537
### 2、树莓派3B+硬件
Raspberry Pi 3 Model B Plus Rev 1.3

### 200208搭建环境
1、官网下载Image（桌面版本）,烧录到SD卡中，上电即可启动。
2、配置。命令sudo raspi-config，修改密码，配置wifi
3、无显示器情况下，需要在SD卡中的/boot目录下建立ssh和wpa_supplicant.conf文件
4、使用VNC远程桌面登录树莓派
### 200209 Linux基本操作
1、ls, cd, mkdir,touch, cp, mv, chmod, pwd...
2、vim基本操作i-当前字符插入，o-下一行插入，a-下一个字符插入
3、vim基本操作G-跳转到最后一行，gg调整到第一行，0-行首，$-行末，数字+Enter-向下移动N行
4、vim基本操作ndd-删除，yy复制，p-粘贴，u-复原前一个操作
5、安装软件sudo apt-get install update
6、固定Ethernet IP地址 sudo vim /ect/dhcpcd.conf --->末尾加入static ip_address = 102.168.0.10
7、markdown轻量级标记语言。标题分级###，*斜体*,**粗体**,~~删除~~,'重点'
### 200211 GPIO操作，python3
1、gpio readall，读出GPIO的配置说明
2、python3,进入python环境中
3、import RPi.GPIO as GPIO   GPIO.setmode(GPIO.BCM)   GPIO.setwarning(False)
4、GPIO.setup(channel,GPIO.OUT)   GPIO.output(channel,LOW)  GPIO.output(HIGH)

