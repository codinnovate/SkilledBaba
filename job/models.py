from django.db import models
import json
from django.contrib.auth.models import User
from datetime import datetime, date


job_type = (
    ('Remote', 'Remote'),
    ('InOffice', 'In-Office')
)

Colors = (
    ('bg-[#3e06e5]', 'blue'),
    ( '#ff758c', 'pink'),
    ( '#764ba2', 'puple'),
    ( '#ff7eb3', 'pink2'),
    ( '#66a6ff', 'lightblue'),
    ( '#fad0c4', 'orangy'),
    ( '#fcb69f', 'lightorangy'),
    ( '#ff9a9e', 'orangy2'),
    ( '#f80759', 'redy'),
    ('#38ef7d', 'greeny'),
    ( '#f7b733', 'yellowy')



)
class Tag(models.Model):
    name = models.CharField(max_length=233, blank=False, null=False)
    def __str__(self):
        return self.name
    

class Company(models.Model):
    name = models.CharField(max_length=233, blank=False, null=False)
    logo = models.ImageField(blank=False, null=False, upload_to='jobs/companies/logos')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ('Companies')
    
    def register(self):
        with open('company.txt', 'a+') as company:
            name = self.name
            json.dump(name, company)



class Job(models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    details = models.TextField(blank=False, null=True)
    company = models.ForeignKey(Company, blank=False, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    color = models.CharField(choices=Colors, default='#66a6ff', max_length=200, null=True, blank=True)
    tag = models.ManyToManyField(Tag)
    salary = models.CharField(max_length=250, blank=False, null=True)
    apply_button = models.URLField(blank=True, null=True)
    deadline = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=500)
    job_type = models.CharField(choices=job_type,max_length=200, null=True, blank=True)


    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    img = models.ImageField(upload_to='blog', null=True)
    details = models.TextField(blank=False, null=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    tag = models.ManyToManyField(Tag)
 

    def __str__(self):
        return self.title
    
class School(models.Model):
    name = models.CharField(max_length=233, blank=False, null=False)
    logo = models.ImageField(blank=False, null=False, upload_to='scholarships/school/logos')
    def __str__(self):
        return self.name 
    
    
class Scholarship(models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    img = models.ImageField(upload_to='scholarship', null=True, blank=True)
    body = models.TextField(blank=False, null=True)
    school = models.ForeignKey(School, blank=False, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    post_date = models.DateTimeField(auto_now_add=True)
    apply_button = models.URLField(blank=True, null=True)
    deadline = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.title