from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
class department(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name
class userInfo(models.Model):
    name = models.CharField(verbose_name="姓名",max_length=16)
    password = models.CharField(verbose_name="密码",max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField("账户余额",max_digits=10,decimal_places=2,default=0)
    creat_time = models.DateTimeField("入职时间")
    depart = models.ForeignKey(to="department",to_field="id",on_delete=models.CASCADE)
    gender_choices = (
        (1,"男"),
        (2,"女")
    )
    gender = models.SmallIntegerField(verbose_name="性别",choices=gender_choices)