import requests
from django.db import models
from django.db.models import TextField, ForeignKey, CASCADE, BooleanField, URLField, IntegerField, CharField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Section(models.Model):
    name = CharField(unique=True, max_length=30)

    def __str__(self):
        return self.name


class Site(models.Model):
    name = CharField(unique=True, max_length=50)
    description = TextField(unique=True, max_length=1000)
    url = URLField()
    section = ForeignKey(Section, on_delete=CASCADE)
    active = BooleanField(default=False)
    hits = IntegerField(default=0)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Site)
def check_active(sender, instance, created, **kwargs):
    if created:
        update_site(instance)


def update_sites():
    for site in Site.objects.all():
        update_site(site)


def update_site(site):
    print(f'Testing availability for site {site.name}')
    try:
        response = requests.get(site.url)
        site.active = response.status_code == 200
    except:
        site.active = False
    site.save()
