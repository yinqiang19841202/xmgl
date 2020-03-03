
from django  import  forms
#自动生成UUID #
from django.db import models
import uuid
#自动生成UUID  end #

app_label = 'xmgl'


class Xmgl_addForm(forms.Form):
    # 自动生成UUID  写法#
    xmbh = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # 项目编号UUID
    # 自动生成UUID 写法 end #
    xmmc = forms.CharField(label="项目名称", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    xmjl = forms.CharField(label="项目经理", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    xmlxdh = forms.CharField(label="项目联系电话", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    bz = forms.CharField(label="备注", max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))





