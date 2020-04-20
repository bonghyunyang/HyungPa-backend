SECRET_KEY = 'j#-&-(11+@m@%-dm0x3-@(64t)nav(61g9r0cv_$#_5r*=h@y%'

DATABASES = {
	'default' : {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'project_1st',
		'USER': 'root',
		'PASSWORD': '',
		'HOST': '127.0.0.1',
		'PORT': '3306',
		'OPTIONS': {'charset': 'utf8mb4'},
		'TEST': {
			'CHARSET': 'utf8mb4',
			'COLLATION': 'utf8_general_ci'
		}
	}
}