from django.db import models

# Create your models here.


class ProfsManager(models.Manager):

    def get_by_natural_key(self, full_name, name_code):
        return self.get(full_name=full_name, name_code=name_code)

class Profs(models.Model):
    full_name = models.CharField("Professor's full name",max_length=20)
    name_code = models.CharField("Proffessor's abbreviated name", max_length=5)
    objects = ProfsManager()

    # class Meta:
    #     unique_together = [['full_name', 'name_code']]

    def natural_key(self):
        return (self.full_name, self.name_code)

    def __str__(self) -> str:
        return "%s"%(self.full_name)



class Modules(models.Model):
    code_by = models.CharField("Module abbreviation", max_length=10)
    full_name = models.CharField("Module's full name", max_length=20)
    semester = models.IntegerField("Semester this module is being taught")
    year = models.IntegerField("Year module is taught")
    prof = models.ManyToManyField(Profs)

   

    def __str__(self) -> str:
        return "%s %s"%(self.code_by,self.full_name)

class Ratings(models.Model):
    profs =models.ManyToManyField(Profs)
    modules=models.ForeignKey(Modules,on_delete=models.CASCADE)
    rating = models.SmallIntegerField("Proffessor rating")
    # def __str__(self) -> str:
    #     return "%d"%(self.rating)
    