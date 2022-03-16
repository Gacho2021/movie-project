from django.test import TestCase
from django.contrib.auth.models import user
from .models import TechType, Movie, Review
import datetime
from  .forms import MovieForm
from django.urls import reverse_lazy, reverse

class TechTypeTest(TestCase):
    def setup(self):
     self.type=TechType(typename='The Batman Fresh')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'The Batman Fresh')

    def test_tablename(self):
        self.assertEqual(str(TechType._meta.db_table), 'techtype')

class movieTest(TestCase):
    def setup(self):
        self.type=TechType(typename='The Batman')
        self.user=user(username='user1')
        self.movie= movie(moviename='Fresh',movietype=self.type, user=self.user, dateentered=date('2/10/2022'),year=2022,movieurl='http://www.Fresh.com',description="The Batman Fresh")

    def test_string(self):
        self.assertEqual(str(movie), 'Fresh')


    def test_cinema(self):
        cine = self.movie.year (2022)
        self.assertEqual(self.movie.cinemaAmount(), cine)

    def test_cinemaAmount(self):
        cine=self.movie.year (2022)
    self.assertEqual(self.movie.cinemaYear(),cine)

class newMovieForm(TestCase):
        #valid form data
    def test_movieForm(self):
        data={
            'moviename':':Drama',
                'movietype' :'The Batman', 
                'user':'Tegen''dateentered''February 28, 2022',
                'year': '2022'
                'movieurl' 'https://www.youtube.com'
                'discription'' New 2022 movies'

            }
        form=MovieForm (data)
    self.assertTrue(form.is_valid)

    def test_movieForm_Invalid(self):
        data={
            'moviename':':Drama',
                'movieype' :'Fresh', 
                'user':'Tegen''dateentered''2022-28-2',
                'movieurl': 'https://www.youtube.com',
                'discription':'New 2022 movies'
         }

        form=MovieForm (data)
    self.assertFalse(form.is_valid)

class New_Movie_Authentication_Test(TestCase):
    def setup(self):
        self.test_user=User .objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.type=Type.objects.create(typename='The Batman')
        self.movie=Movie.objects.create(moviename='Fresh',movietype=self.type, user=self.test_user, dateentered=date('2/28/2022'),year=2022,movieurl='http://www.youtube.com',description="the batman fresh")

    def test_redirect_if_not_logged_in(self):
        response.self.client.get(reverse('newmovie'))
        self.assertRedirects(response,'accounts/login/?next=tech/newmovie')
