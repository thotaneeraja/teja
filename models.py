from django.db import models
class test(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    costperitem=models.DecimalField(max_digits=10,decimal_places=2)
    stockquantity=models.DecimalField(max_digits=10,decimal_places=3)
    volume=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)

    def calc_volume(self):
        v=self.costperitem*self.stockquantity
        return v
    def save(self,*args,**kwargs):
        self.volume=self.calc_volume()
        super(test,self).save()
    def __str__(self):
        return self.name


# Create your models here.
