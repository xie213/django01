from django.db import models

# python3 manage.py makemigrations 将操作记录记录到小本本上(migrations文件夹)
#
# python3 manage.py migrate  将操作真正的同步到数据库中
# # 只要你修改了models.py中跟数据库相关的代码 就必须重新执行上述的两条命令


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64)
    passwrod = models.IntegerField()
    info = models.CharField(max_length=62,verbose_name='个人简绍',null=True)
    hobby = models.CharField(max_length=64,verbose_name='兴趣爱好',default='学生')
