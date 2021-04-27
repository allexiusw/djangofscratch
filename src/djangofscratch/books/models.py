from django.db import models
from django.utils.html import mark_safe

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name.title()


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(verbose_name='e-mail')
    
    class Meta:
        ordering = ['last_name']

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return (self.last_name+" "+self.first_name).title()


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.title.title()

    @property
    def authors_list(self):
        dev =''
        authors = self.authors.all()
        if authors is not None:
            for author in authors:
                dev+=author.first_name+"<br>"
        dev = mark_safe(dev)
        return dev



class Country(models.Model):
    name = models.CharField("Nombre", max_length=200)
    country_code = models.CharField("Código de país", max_length=10, default='503')
    flag = models.CharField('Bandera', max_length=10, default='lag-icon flag-icon-slv')

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField("Nombre", max_length=200)
    edad = models.IntegerField("Edad", default=18)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return self.name
        