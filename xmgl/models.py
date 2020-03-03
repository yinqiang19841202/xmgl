from django.db import models
import uuid


# Create your models here.
class Xmgl(models.Model):


    xmbh = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)#项目编号
    xmmc = models.CharField(max_length=256,unique=True)#项目名称
    xmjl = models.CharField(max_length=32)#项目经理
    xmlxdh = models.CharField(max_length=32)#项目联系电话
    bz = models.CharField(max_length=500)#备注信息
    c_tmie = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.xmmc

    class Meta:
        #ordering = ["-c_time"]
        verbose_name = "项目管理"
        verbose_name_plural = "项目管理"