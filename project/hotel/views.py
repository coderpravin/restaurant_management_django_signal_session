from django.shortcuts import render, redirect, HttpResponse
from .models import Customer
from django.contrib.auth.hashers import check_password
from django.dispatch import Signal

# Create your views here.

def homeHotel(request):
    return render(request, "hotel/homeHotel.html")

def viewCustomer(request):
    customers = Customer.objects.all()    
    return render(request, "hotel/customerHotelHome.html", {'customers':customers})

customer_logged_in = Signal()

def loginCustomer(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:

            customer = Customer.objects.get(email=email)
            if check_password(password, customer.password):
                request.session['customer_id'] = customer.id
                customer_logged_in.send(sender=Customer, customer=customer)
                return redirect("customerHome")
            else:
                return HttpResponse("Not Login")
            
        except Customer.DoesNotExist:
            return HttpResponse("Customer is not present")
            
    return render(request, "hotel/customer-login.html")


customer_logged_out = Signal()
def logoutCustomer(request):
    customer_id = request.session.get('customer_id')
    if customer_id:
        try:
            customer = Customer.objects.get(id=customer_id)
            customer_logged_out.send(sender=Customer, customer=customer)
        except Customer.DoesNotExist:
            pass

    request.session.flush()
    return redirect("homeHotel")


def signupCustomer(request):
    if request.method == "POST":
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        city = request.POST.get("city")
        age = request.POST.get("age")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        password = request.POST.get("password")

        customer = Customer(first_name=first_name, last_name=last_name, city=city, age=age, mobile=mobile, email=email, password=password)

        customer.save()
        return redirect('loginCustomer')

    return render(request, "hotel/customer-signup.html")

def customerHome(request):
    return render(request, "hotel/customer-home.html")

