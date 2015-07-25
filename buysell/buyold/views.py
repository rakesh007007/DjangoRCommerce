from django.shortcuts import render
import buyold.views
from django.template.response import TemplateResponse
from django.template import Context, loader
from django.http import HttpResponse
from django.contrib import sessions
from django.middleware import csrf
from buyold.models import *
from buysell.settings import *
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import redirect
import logging
from django.core.files.storage import default_storage
logger = logging.getLogger(__name__)
from django.core.files.base import ContentFile

# Create your views here.
def get_or_create_csrf_token(request):
    token = request.META.get('CSRF_COOKIE', None)
    if token is None:
        token = csrf._get_new_csrf_key()
        request.META['CSRF_COOKIE'] = token
    request.META['CSRF_COOKIE_USED'] = True
    return token
def register(request):
	 
	 return TemplateResponse(request, 'index.html',{'csrf_token':get_or_create_csrf_token(request)})
def addProduct(request):
	if ('loggedin' not in request.session):
		return redirect('/login')
	else:
		categories = Category.objects.all()
		return TemplateResponse(request, 'addproduct.html',{'categories':categories,'csrf_token':get_or_create_csrf_token(request)})
def main(request):
	if ('loggedin' not in request.session):
		return redirect('/login')
	else:
		items = Item.objects.all()
		images = Productimage.objects.all()
		logger.debug('starts fro here')
		logger.debug(MEDIA_ROOT)
		logger.debug('ends fro here')
		return TemplateResponse(request, 'main.html',{'images':images,'csrf_token':get_or_create_csrf_token(request),'items':items})

def cart(request):
	if ('loggedin' not in request.session):
		return redirect('/login')
	else:
		userId = request.session['email_id']
		user =User.objects.filter(email_id=userId)[0]

		items = Cartitems.objects.filter(user = user)
		return TemplateResponse(request, 'cart.html',{'csrf_token':get_or_create_csrf_token(request),'items':items})

		
def login(request):
	if ('loggedin' not in request.session):
		return TemplateResponse(request, 'login.html',{'csrf_token':get_or_create_csrf_token(request)})
	else:
		return redirect('/main')

def logPost(request):
	email_id = request.POST['email_id']
	password = request.POST['password']
	u= User.objects.filter(email_id=email_id).filter(password=password)
	if(len(u)>0):
		request.session['loggedin']=True
		request.session['email_id'] = email_id
		return redirect('/main')
	else:
		return redirect('/login')
def handle_uploaded_file(f,name):
    with open('media/'+name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def logout(request):
	 del request.session['loggedin']
	 del request.session['email_id']
	 return HttpResponse('logged out')
def productPost(request):
	 name= request.POST['name']
	 conditions= request.POST['conditions']
	 userId = request.session['email_id']
	 #categories = request.POST['categories']
	 from PIL import Image
	 

	 #handle_uploaded_file(request.FILES['image'],'rakesh.jpg')
	 #logging.debug(image)
	 #category = Category.objects.filter(name=categories)[0]
	 user = User.objects.filter(email_id = userId)[0]




	 rak = Item();
	 images=request.FILES.getlist('image')
	 rak.name = name
	 rak.coverphoto = images[0]
	 rak.conditions = conditions
	 rak.user = user
	 #rak.image = image
	 #rak.categories.add(category)
	 rak.save()
	 item_id = rak.item_id
	 for afile in request.FILES.getlist('image'):
	 	logging.debug(afile)
	 	d = Productimage()
	 	d.item_id = item_id
	 	d.image = afile
	 	d.save()



	 return HttpResponse('yo it works')
def addItemPost(request):
	 productId= request.POST['item_id']
	 userId = request.session['email_id']
	 user = User.objects.filter(email_id = userId)[0]
	 product = Item.objects.filter(item_id = productId)[0]




	 rak = Cartitems();
	 rak.item = product
	 rak.user = user
	 rak.save()
	 return HttpResponse('yo you have qaded items to cart!! works')
def productView(request):
	 productId= request.POST['item_id']
	 images = Productimage.objects.all()
	 product = Item.objects.filter(item_id = productId)[0]

	 return TemplateResponse(request, 'view.html',{'images':images,'product':product,'csrf_token':get_or_create_csrf_token(request)})
def removeItemPost(request):
	 productId= request.POST['item_id']
	 userId = request.session['email_id']
	 user = User.objects.filter(email_id = userId)[0]
	 product = Item.objects.filter(item_id = productId)[0]




	 Cartitems.objects.filter(user=user).filter(item=product).delete()


	 return HttpResponse('yo you have remove item from cart!! works')

def regPost(request):
	 s = SessionStore()
	 house_no = request.POST['house_no']
	 mob= request.POST['mob']
	 password= request.POST['password']
	 pincode = request.POST['pincode']
	 town = request.POST['town']
	 city = request.POST['city']
	 name= request.POST['name']
	 enno= request.POST['enno']
	 email_id = request.POST['email_id']




	 rak = Address();
	 rak.house_no = house_no
	 rak.city = city
	 rak.pincode = pincode
	 rak.town = town
	 rak.mob= mob
	 rak.save()
	 idd = rak.address_id
	 rak2 = User();
	 rak2.name = name
	 rak2.mob= mob
	 rak2.enno = enno
	 rak2.email_id = email_id
	 rak2.password = password
	 rak2.address = rak
	 rak2.save()


	 return HttpResponse('yo it works')
	 

