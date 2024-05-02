from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField(max_length=300)
    number = models.IntegerField(True)
    photo = models.ImageField(blank=False, upload_to="images")
    class Meta:
        verbose_name_plural = "MyModel"
    def __str__(self):
        return self.name

class MyModel2(models.Model):
    title = models.CharField(max_length=50 )
    description = models.TextField(max_length=300)
    amount = models.IntegerField(True)
    image = models.ImageField(blank=False, upload_to="images")
    field_name = models.FileField(upload_to=None, max_length=150)

    class Meta:
        verbose_name_plural = "MyModel2"

    def __str__(self):
        return self.title
class MyModel3(models.Model):    
    message = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "MyModel3"
    def __str__(self):
        return self.message



    
    