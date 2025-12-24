
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY='dev'
DEBUG=True
ALLOWED_HOSTS=[]
INSTALLED_APPS=[
 'django.contrib.staticfiles',
 'website',
]
MIDDLEWARE=[]
ROOT_URLCONF='core.urls'
TEMPLATES=[{
 'BACKEND':'django.template.backends.django.DjangoTemplates',
 'DIRS':[BASE_DIR/'website/templates'],
 'APP_DIRS':True,
}]
WSGI_APPLICATION='core.wsgi.application'
DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
LANGUAGE_CODE='pt-br'
TIME_ZONE='America/Sao_Paulo'
STATIC_URL='/static/'
STATICFILES_DIRS=[BASE_DIR/'website/static']
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
