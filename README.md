# mysite

>*  django-cors-headers

安装:

```python  
pip install django-cors-headers
```

配置（两步）

1.settings.py 修改

```python  
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    **'corsheaders.middleware.CorsMiddleware',**
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

2.settings.py 添加

```python  
CORS_ORIGIN_ALLOW_ALL = True
```
