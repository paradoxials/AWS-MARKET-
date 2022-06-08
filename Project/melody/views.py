from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import *
from .models import *

# Create your views here.
# Bolabola - dashboard and song registration
# Sison - index or landing page and customer registration
# userID = 0
class MelodyIndexView(View):
	def get(self, request):
		return render(request, 'melody/index.html')
	def post(self, request):
		global userID
		if request.method == 'POST':
			if 'btnLogin'in request.POST:
				email = request.POST.get("email")
				password = request.POST.get("password")
				user = Customer.objects.get(email = email, password = password)
				userID = user.id
			return redirect('melody:melody_customerDashboard_view')

class MelodyProductDashboardView(View):
	def get(self, request):
		global userID
		songs = Song.objects.all()
		user = Customer.objects.get(id = userID)
		context={
			'songs' : songs,
			'user' : user,
		}
		return render(request, 'melody/productDashboard.html', context)
	def post(self, request):
		if request.method == 'POST':
			global userID
			if 'btnUpdate' in request.POST:
				sid = request.POST.get("song-id")
				title = request.POST.get("song-title")
				date = request.POST.get("song-release")
				artist = request.POST.get("song-artists")
				genre = request.POST.get("song-genre")
				writers = request.POST.get("song-writer")
				producer = request.POST.get("song-producer")
				# img = request.FILES["coverphoto"]
				# print(img)
				update_song = Song.objects.filter(id = sid).update(songtitle = title, genre = genre, artist = artist, 
								dateRelease = date, producer = producer, songwriter = writers)
				print(update_song)
			elif 'btnDelete' in request.POST:
				sid = request.POST.get("song-id")
				song = Song.objects.filter(id = sid).delete()
				print('record deleted')
			elif 'btnFilter' in request.POST:
				startdate= request.POST.get("datepicker_from")
				enddate =  request.POST.get("datepicker_to")
				songs = Song.objects.filter(dateRelease__range=(startdate,enddate))
				user = Customer.objects.get(id = userID)
				context = {
					'songs' : songs,
					'user' : user,
				}
				return render(request, 'melody/productDashboard.html', context)
			return redirect('melody:melody_productDashboard_view')

class MelodyCustomerDashboardView(View):
	def get(self, request):
		global userID
		customers = Customer.objects.all()
		user = Customer.objects.get(id = userID)
		context = {
			'customers' : customers,
			'user' : user,
		}
		return render(request, 'melody/customerDashboard.html', context)
	def post(self, request):
		global userID
		if request.method == 'POST':
			if 'btnUpdate' in request.POST:
				cid = request.POST.get("customer-id")
				fname = request.POST.get("customer-fname")
				lname = request.POST.get("customer-lname")
				date = request.POST.get("customer-bday")
				add = request.POST.get("customer-add")
				email = request.POST.get("customer-email")
				contact = request.POST.get("customer-contact")
				profilepicture = 'images/'+str(request.FILES['profilepicture'])
				update_customer = Customer.objects.filter(id = cid).update(firstname = fname, lastname = lname,
								birthday = date, address = add, email = email, contact = contact, profilepicture = profilepicture)
				
				print(update_customer)
			elif 'btnDelete' in request.POST:
				cid = request.POST.get("customer-id")
				customer = Customer.objects.filter(id = cid).delete()
				print('record deleted')
			elif 'btnFilter' in request.POST:
				startdate= request.POST.get("datepicker_from")
				enddate =  request.POST.get("datepicker_to")
				customers = Customer.objects.filter(birthday__range=(startdate,enddate))
				user = Customer.objects.get(id = userID)
				context = {
					'customers' : customers,
					'user' : user,
				}
				return render(request, 'melody/customerDashboard.html', context)
			return redirect('melody:melody_customerDashboard_view')

class MelodyCustomerRegistrationView(View):
	def get(self, request):
		return render(request, 'melody/customerRegister.html')
	def post(self, request):
		form = CustomerForm(request.POST,request.FILES)
		if form.is_valid():
			fname = request.POST.get("firstname")
			lname = request.POST.get("lastname")
			bday = request.POST.get("birthday")
			add = request.POST.get("address")
			email = request.POST.get("email")
			password = request.POST.get("password")
			contact = request.POST.get("contact")
			# img = request.FILES('profilepicture',False)
			if 'profilepicture' in request.FILES:
				img = request.FILES['profilepicture']
				print(img)
			else:
				img = request.FILES.get('images/avatar.png')
			form = Customer(firstname = fname, lastname = lname, birthday = bday, address = add, email = email,
							password = password, contact = contact, profilepicture = img)
			form.save()
			return redirect('melody:melody_index_view')
		else:
			print(form.errors)
			return HttpResponse("Form is invalid")

class MelodySongRegistrationView(View):
	def get(self, request):
		return render(request, 'melody/songRegister.html')
	def post(self, request):
		form = SongForm(request.POST, request.FILES)	
		if form.is_valid():
			title = request.POST.get("songtitle")
			genre = request.POST.get("genre")
			artist = request.POST.get("artist")
			date = request.POST.get("dateRelease")
			producer = request.POST.get("producer")
			songwriter = request.POST.get("songwriter")
			# if 'songImage' in request.FILES:
			# 	songimg = request.FILES['songImage']
			# 	print(songimg)
			# else:
			# 	songimg = request.FILES.get('images/avatar.png')
			form = Song(songtitle = title, genre = genre, artist = artist, dateRelease = date, producer = producer, 
						songwriter = songwriter)
			form.save()
			return redirect('melody:melody_productDashboard_view')
		else:
			print(form.errors)
			return HttpResponse("Form is invalid")	