from thirdapp.models import product
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render(request,'index.html')
def edit(request,id):
    pro_id=product.objects.get(id=id)
    return render(request,'edit.html',{'id_edit':pro_id})
def add_pro(request):
    if request.method=='POST':
        pro_name=request.POST['pro_name']
        pro_des=request.POST['pro_des']
        pro_qun=request.POST['pro_qun']
        price=request.POST['price']
        pro=product(pro_name=pro_name,pro_des=pro_des,pro_qun=pro_qun,price=price)
        pro.save()
        return redirect('index')
def display(request):
    pro_table=product.objects.all()
    return render(request,'display.html',{'result':pro_table})
def pro_edit(request,id):
    if request.method=='POST':
        pro_item=product.objects.get(id=id)
        pro_item.pro_name=request.POST['pro_name']
        pro_item.pro_des=request.POST['pro_des']
        pro_item.pro_qun=request.POST['pro_qun']
        pro_item. price=request.POST['price']
        pro_item.save()
        return redirect('display')
def pro_del(request,id):
    item_pro=product.objects.get(id=id)
    item_pro.delete()
    return redirect('display')