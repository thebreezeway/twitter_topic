# 安装环境
```shell
pip install django
pip install mysql-connector-python
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

	