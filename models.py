from django.db import models
from django.contrib.auth.models import User

class  TechType(models.Model):
    typename=models.CharField(max_length=154)
    typedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table='techtype'

class movie(models.Model):
    moviename=models.CharField(max_length=154)
    movietype=models.ForeignKey(TechType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateentered=models.DateField()
    year=models.DecimalField(max_digits='4', decimal_places=1)
    movieURL=models.URLField()
    description=models.TextField()

    def __str__(self):
        return self.moviename

    class Meta:
        db_table='movie'

class Review(models.Model):
    title=models.CharField(max_length=154)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    movie=models.ForeignKey(movie, on_delete=models.CASCADE)
    reviewdate=models.DateField()
    reviewtext=models.TextField()

    def cinemaAmount(self):
        self.cinemayear=self.year-cine* .03
        return self.cinema

# it is almost working
    def cinemaYear(self):
        self. cinemaYear=self.Year-self.cinema
        return self.year * .03

       #def cinemaYear(self):


    def __str__(self):
        return self.title

    class Meta:
        db_table='review'
