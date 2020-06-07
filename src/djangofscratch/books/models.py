from django.db import models

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
    email = models.EmailField()
    
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