# sucker  

簡化 Docker 執行參數的工具


# Install  

1. Install fire package  
  `pip install fire`

2. Clone   
  `$ git clone https://github.com/future/sucker`

3. chmod & copy   
  `$ chmod 711 sucker/sucker`  
  `$ sudo cp sucker/sucker /usr/bin/`



# 建立 sucker.ini 設定檔

sucker.ini 設定 container 啟動的各項參數  
socker.ini 會依序從
1. ./socker.ini   
2. ~/.socker/socker.ini    
3. /etc/socker.ini  

第一個存在的 socker.ini 作為設定檔

## [DEFAULT]

預設值; 若其他各 section 重複設定與[DEFAULT]中同名變數則會覆蓋掉預設值

```ini
[DEFAULT]
image = spark/py36:v1
workdir = /opt
rm = yes
stdin = yes
tty = yes
detach = no
```

## [SectionName]

- name : container name (用於識別)
- program : 執行的主程式
- device#n : 多參數在後面加上 #1...#n

```ini
[py3]
name = py3
program = python3
net = host
device#0 = /dev/video0
device#1 = /dev/video1
link = visdom
```



# 執行

第一個參數為 sucker.ini 中 section name    

Ex.
設定檔內容為

```ini
[sh]
...
[cmd]
...
[py3]
...

```
執行時

  sucker **sh**   
  sucker **cmd** ls -lh  
  sucker **py3** example/test.py   
  sucker **jupyter**  
  sucker **jupyterlab**  
