# 安装环境
```shell
pip install django
pip install mysqlclient
cd  '../twitter_topic'   //最外面的文件夹
```

#数据库建表

```shell
python manage.py migrate
python manage.py makemigrations topic_retrieval 
python manage.py sqlmigrate topic_retrieval 0004    
python manage.py migrate 
```

#启动服务器
```shell

python manage.py runserver
```

#修改数据库配置（ip等）
修改 /twitter_topic/twitter_topic/settings.py 文件中的 DATABASES = {}

	话题	相关推文
1	2018-12-28T03:50:24	The G in God is capitalized.The G in God is capitalized.The G in God is capitalized.The G in God is capitalized.The G in God is capitalized.The G in God is capitalized.The G in God is capitalized.The G in God is capitalized.The G in God is capitalized.	
2	2018-12-28T01:25:15	common sense ain’t so common ?	
3	2018-12-27T16:00:05	There are myriad reasons for both a Department of Defense and an Army Regulation against military personnel participating in or showing allegiance to ANY political party while in uniform. Good commanders enforce; good NCOs jerk a knot in the asses of those who violate.	
4	2018-12-27T13:13:53	NIA seized from ISIS Module:1. Rocket launcher2. 25 Kg of Explosives3. 12 Pistols4. Bulletproof vest in the making5. Fake Documents6. ISIS literatureBut Liberals can only see '3 firecrackers' which were also seized.After Urban Naxals, Liberals now defend ISIS Radicals.	
5	2018-12-27T12:42:45	There are myriad reasons for both a Department of Defense and an Army Regulation against military personnel participating in or showing allegiance to ANY political party while in uniform. Good commanders enforce; good NCOs jerk a knot in the asses of those who violate.	
6	2018-12-17T16:51:23	I can’t wait to start saying “Fuck it, it’s Christmas”Fancy a drink tonight? “Fuck it, it’s Christmas” Eat five packs of biscuits? “Fuck it, it’s Christmas”Third night getting pissed in a row? “Fuck it, it’s Christmas”







