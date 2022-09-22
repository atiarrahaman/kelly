from django.db import models
from django.contrib.auth.models import User

# Create yourmode ls here.




class AboutContent(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    designation=models.CharField(max_length=150)
    descption=models.TextField()
    birthday=models.DateField(auto_now=False, auto_now_add=False)
    phone=models.CharField( max_length=150)
    website=models.CharField( max_length=150)
    city=models.CharField( max_length=150)
    age= models.IntegerField()
    education=models.CharField( max_length=150)
    email= models.EmailField( max_length=254)
    status=models.CharField( max_length=150)
    image=models.ImageField(upload_to='image')
    def __str__(self):
        return str(self.id)

class Skill(models.Model):
    username= models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    percent= models.CharField(max_length=150)
    value= models.CharField(max_length=150)
    bg=models.CharField(max_length=150)
    def __str__(self):
        return self.name
    
    
class Countup(models.Model):
    username= models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField( max_length=150)
    count= models.IntegerField()
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    username= models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    designation= models.CharField(max_length=150)
    des= models.TextField()
    img= models.ImageField( upload_to='TestiImage')
    def __str__(self):
        return self.name
    

class  Education (models.Model):
    username= models.ForeignKey(User, on_delete=models.CASCADE)
   
    degree= models.CharField(max_length=150)
    start_date= models.DateField()
    end_date= models.DateField(null=True ,blank=True)
    inistitute=models.CharField( max_length=150)
    des=models.TextField()
    def __str__(self):
        return str(self.username)


class  Summary (models.Model):
    username= models.OneToOneField(User, on_delete=models.CASCADE)
    descptions= models.TextField()
    address= models.CharField(max_length=150)
    phone= models.CharField( max_length=150)
    email= models.EmailField()
    
    def __str__(self):
        return str(self.username)
class  ProfesionalExperience (models.Model):
    username= models.ForeignKey(User, on_delete=models.CASCADE)
   
    designation= models.CharField(max_length=150)
    start_date= models.DateField()
    end_date= models.DateField(null=True ,blank=True)
    inistitute=models.CharField( max_length=150)
    des=models.TextField()
    def __str__(self):
        return str(self.username)

class ServicePart(models.Model):
    username= models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField( max_length=150)
    descption= models.TextField()
    icon= models.ImageField(upload_to='service-icon')

class Map(models.Model):
    username= models.OneToOneField(User, on_delete=models.CASCADE)
    maps=  models.TextField()