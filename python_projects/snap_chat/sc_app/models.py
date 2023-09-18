from django.db import models

# Create your models here.
class Coder(models.Model):
    """Model to store coder aspects"""
    nick_name = models.CharField(max_length = 25)

    def __str__(self):
        return self.nick_name
class Code(models.Model):
    """Storage class for the code"""
    pub_date = models.DateField(auto_now=True)
    descp = models.CharField(max_length= 200) # short description of code
    upd_date = models.DateTimeField(auto_now_add=True)
    code_desc = models.TextField()
    coder = models.ForeignKey(Coder,on_delete = models.CASCADE)

    def __str__(self):
        return self.descp