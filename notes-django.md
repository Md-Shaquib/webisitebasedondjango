— virtualenv -p python3 . | virtualenv venv
source bin/activate
pip install django
django-admin
django-admin startproject mywebpage .
python manage.py runserver
python manage.py startapp home
//Add app in settings.py
model.py
class Product (models.Model):
              Name = models.textfield()
 python manage.py makemigrations
python manage.py migrate
//Add from .models import Product in admin.py
//Add admin.site.register(Product)
Start from 42.35
python manage.py shell
from home.models import Product
Product.objects.all()
Product.objects.create(title=“”,description=“”,price=“”)
summary = models.TextField(default=“Hello”)
// Models
	title = models.CharField(max_length=120) #when using 	charfield max length is mandatory
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(decimal_places=2,max_digits=10000)
	summary = models.TextField(default="Hello")
	featured = models.BooleanField(default=True)
// Views.py
def home(requests,*args,**kwargs):
    return render(requests,”home.html”,{})

// Create templates folder inside it create htmls files

// updating setting in setting        'DIRS': [os.path.join(BASE_DIR,"templates")],

// create a forms.py in app
Use from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
