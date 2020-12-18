from django.db import models
from django.conf import settings
from django.core.serializers import serialize
import json

# Create your models here.

def upload_update_image(instance,filename):
    return "app/{user}/{filename}".format(user=instance.user,filename=filename)


class UpdateQuerySet(models.QuerySet):
    # def serialize(self):
    #     qs=self
    #     return serialize("json",qs,fields=('user','content','image'))

    # def serialize(self):
    #     qs=self
    #     final_array = []
    #     for obj in qs:
    #         stuct = json.loads(obj.serialize())
    #         final_array.append(stuct)
    #     return json.dumps(final_array)

    def serialize(self):
        list_values = list(self.values('user','content','image'))
        return json.dumps(list_values)

class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model,using=self._db)



class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_update_image,null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    # Converting our data  to different data structure is called serialization

    # def serialize(self):
    #     """
    #     returns only one obj json dict
    #     """

    #     json_data = serialize("json",[self],fields=('user','content','image'))
    #     stuct = json.loads(json_data) # [{}]
    #     data = json.dumps(stuct[0]['fields'])

    #     return data
        # return json_data = serialize("json",[self],fields=('user','content','image'))
    def serialize(self):
        try:
           image = self.image.url
        except:
            image = ""

        data ={
            "content" : self.content,
            "user": self.user.id,
            "image": image
        }
        
        data = json.dumps(data)
        return data


