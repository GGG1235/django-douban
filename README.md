# django-douban

用django输出mysql中的信息.

### 环境:

django2.1.2

Python3.7.0

mysql5.7.22

macOS Mojave 10.14.3


### 数据库设置 

将settings.py中的DATABASES改为如下:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_douban',
        'USER':'root',
        'PASSWORD':'1997',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}
```


在settings.py中设置静态文件路径```STATIC_URL = '/static/'```

### 截图:

<img src="https://github.com/GGG1235/django-douban/blob/master/images/page1.png" width="375" alt="neofetch">

<img src="https://github.com/GGG1235/django-douban/blob/master/images/page2.png" width="375" alt="neofetch">

<img src="https://github.com/GGG1235/django-douban/blob/master/images/page3.png" width="375" alt="neofetch">

<img src="https://github.com/GGG1235/django-douban/blob/master/images/info.png" width="375" alt="neofetch">
