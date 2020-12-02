from django.db import models

class CatBreed(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return F"{self.name}"

class Cat(models.Model):
    name = models.CharField(max_length=255)
    cat_breed = models.ForeignKey(CatBreed,
                                  on_delete=models.SET_NULL,
                                  null=True)

    def __str__(self):
        return F"{self.name}, {self.cat_breed}"
