from django.http import HttpResponse
from django.shortcuts import render
from django.template import  loader

# Create your views here.

from django.shortcuts import redirect
from . import models
from . import forms

def xmgl(request):
    # xmgl_detail = Xmgl.objects.all()
    xmgl_details = models.Xmgl.objects.all()
    template = loader.get_template('xmgl/xmgl.html')
    context = {
        'xmgl_details':xmgl_details
    }
    return  HttpResponse(template.render(context,request))
    # return render(request, 'xmgl/xmgl.html')
    # return render(request,'xmgl/xmgl.html',locals())

def yinq(request):
    pass
    return render(request, 'xmgl/yinq.html')



def xmgl_add(request):
    # if request.session.get('is_login', None):
    #     return redirect('/index/')

    if request.method == 'POST':
        xmgl_add_form = forms.Xmgl_addForm(request.POST)
        message = "请检查填写的内容！"
        if xmgl_add_form.is_valid():
            xmmc = xmgl_add_form.cleaned_data.get('xmmc')
            xmjl = xmgl_add_form.cleaned_data.get('xmjl')
            xmlxdh = xmgl_add_form.cleaned_data.get('xmlxdh')
            bz = xmgl_add_form.cleaned_data.get('bz')

            ##########判断 项目名称是否相同
            same_name_xmmc = models.Xmgl.objects.filter(xmmc=xmmc)
            if same_name_xmmc:
                message = '项目名已经存在'
                return render(request, 'xmgl/xmgl_add.html', locals())


            new_xmgl = models.Xmgl()
            new_xmgl.xmmc = xmmc
            new_xmgl.xmjl = xmjl
            new_xmgl.xmlxdh = xmlxdh
            new_xmgl.bz = bz
            new_xmgl.save()

            return redirect('xmgl:xmgl')
        else:
            return render(request, 'xmgl/xmgl_add.html', locals())
    xmgl_add_form = forms.Xmgl_addForm()
    return render(request, 'xmgl/xmgl_add.html', locals())