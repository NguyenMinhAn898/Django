from django.db import models

# Create your models here.

# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     name = models.CharField(max_length=200, null=True)
#     email = models.EmailField(unique=True, null=True)
#     # bio = models.TextField(null=True)

#     # avatar = models.ImageField(null=True, default="avatar.svg")

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []


class Category(models.Model):
    name = models.CharField(max_length=250, null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=250, null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.TextField(max_length=250, null=False)
    detail = models.TextField(max_length=250, null=False)
    description = models.TextField(max_length=2500, null=False)    
    imgUrl = models.TextField(max_length=500,null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    places = models.ManyToManyField(
        Place, related_name='participants', blank=True)
    publicDate = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ['-updated', '-created']

    def get_Place(self):
        ret = ''
        for dept in self.places.all():
            ret = ret + dept.name + ', '
        # remove the last ',' and return the value.
        return ret[:-1]

    def get_PublicDate_Str(self):
        if(self.publicDate != None):
            return self.publicDate.strftime('%Y-%m-%d')
        return ''
