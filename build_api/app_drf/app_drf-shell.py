from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from app_drf.serializers import StatusSerializer,CustomSerializer
from app_drf.models import Status

'''
Serialize a Single Object
'''

obj = Status.objects.first()
serializer = StatusSerializer(obj)
serializer.data
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)


'''
Serialize a QuerySet
'''

qs = Status.objects.all()
serializer2 = StatusSerializer(qs,many=True)
serializer2.data
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data2)

stream2 = BytesIO(json_data2)
data2 = JSONParser().parse(stream2)
print(data2)


'''
Create Object
'''
data = {
    "user" :1
}

create_serializer = StatusSerializer(data=data) #ModelSerializer
create_serializer.is_valid() # Same like forms
create_serializer.save()

'''
Update Object
'''
data = {
    "user" :1
    "content" : "Some new content"
}
obj = Status.objects.first()

update_serializer = StatusSerializer(obj,data=data)
update_serializer.is_valid() # Same like forms
update_serializer.save() # returns instance of object

'''
Delete Object
'''
obj = Status.objects.last()
obj.delete()



'''
CustomSerializer 

'''

data ={
    "email" : "test@gmail.com",
    "content" : "Test data"
}

create_obj_serializer = CustomSerializer(data)
if create_obj_serializer.is_valid():
    data = create_obj_serializer.data
    print(data)
