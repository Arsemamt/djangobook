from django.db import models

class CompanyInformation(models.Model):
   name  = models.CharField(max_length=100)
   description = models.TextField()
   
   def __str__(self) -> str:
        return self.name
  
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Book(models.Model):
    image = models.ImageField()#null=True
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField()
    price = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    
    # genre = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title