from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Product, Order

def Loginviews(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password= password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('Addproduct')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form, 'title':'log in'})

def Addproduct(request):
    if request.method=="POST":
        name = request.POST['name']
        category = request.POST['category']
        quantity = request.POST['quantity']
        description = request.POST['description']
        new_emp = Product(name=name, category=category, quantity=quantity, description=description)
        new_emp.save()
        return redirect('helloView')
    else:
        return render(request, "addbook.html")

def helloView(request):
    books=Product.objects.all()
    return render(request,"viewbook.html",{"books":books})

def editproduct(request):
    if request.method=="POST":
        n=request.POST["name"]
        c=request.POST["category"]
        q = request.POST['quantity']
        d = request.POST['description']
        product=Product.objects.get(id=request.GET['id'])
        product.name=n
        product.category=c
        product.quantity=q
        product.description=d
        product.save()
        return HttpResponse('successfully') 

def editProductView(request):
    editbook=Product.objects.all()
    print(editbook)
    return render(request,"edit-book.html",{"editbook":editbook}) 

def delete(request, id):
  member = Product.objects.get(id=id)
  member.delete()
  return HttpResponse('delete successfully')

def order(request):
    if request.method=="POST":
        product = request.POST['product']
        created = request.POST['created']
        o_quantity = request.POST['o_quantity']
        date = request.POST['date']
        order_data = Order(product=product, created=created, o_quantity=o_quantity, date=date)
        order_data.save()
        return redirect('orderview')
    else:
        return render(request, "order.html")
    
def OrderView(request):
    orders=Order.objects.all()
    return render(request,"addorder.html",{"orders":orders})