from django.shortcuts import render, HttpResponse, redirect
from app01.models import user
from app01 import models
from django import forms


# Create your views here.
class MyForm(forms.ModelForm):
    class Meta:
        model = models.userInfo
        fields = ['name', 'password', 'age', 'account', 'creat_time', 'gender', 'depart']
        widgets = {
            "password":forms.PasswordInput(attrs={"class":"form-control"})#必须双引号
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # print(name, field)
            if name == 'password':
                continue
            field.widget.attrs = {"class":"form-control","placeholder":field.label}


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # 如果是POST请求，获取用户提交的数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = user.objects.filter(name=username).first()  # 获取账号对应的数据表
        print(obj)
        if obj != None:
            if username == obj.name and password == obj.password:
                return HttpResponse("登陆成功")
            else:
                return render(request, 'login.html', {'error_msg': '账号名或密码错误'})
        else:
            return render(request, 'login.html', {'error_msg': '账号不存在'})


def orm(request):
    user.objects.create(name='wlj', password='520999', age=20)  # 增
    # 删查
    # user.objects.filter(id=1).delete()
    # user.objects.all()
    return HttpResponse("成功")


def user_list(request):
    querset = models.department.objects.all()
    return render(request, 'user_list.html', {'querset': querset})  # 根据App的注册顺序主意去他们的templates去找


def department_add(request):
    if request.method == 'GET':
        return render(request, 'department_add.html')
    else:
        id = request.POST.get('id')
        name = request.POST.get('name')
        if models.department.objects.filter(id=id).first() == None and models.department.objects.filter(
                name=name).first() == None:
            models.department.objects.create(id=id, name=name)
        return redirect('/user/list')


def department_delete(request):
    nid = request.GET.get('nid')
    models.department.objects.filter(id=nid).delete()
    return redirect('/user/list')


def department_edit(request, nid):
    if request.method == 'GET':
        obj = models.department.objects.filter(id=nid).first()
        return render(request, 'department_edit.html', {'obj': obj})
    id = request.POST.get('id')
    name = request.POST.get('name')
    if id == '' or models.department.objects.filter(id=id).first() != None:
        id = nid
    if name != '':
        models.department.objects.filter(id=nid).update(id=id, name=name)
    else:
        models.department.objects.filter(id=nid).update(id=id)
    return redirect('/user/list')


def user(request):
    data = models.userInfo.objects.all()
    return render(request, 'user.html', {'data': data})


def user_add(request):
    form = MyForm()
    return render(request, 'user_add.html', {'from': form})
