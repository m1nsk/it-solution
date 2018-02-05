from django.http import HttpResponse, Http404
from .models import Transfer
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def get_data(request):
    if request.method == 'GET':
        id = int(request.GET.get('id', -1))
        if id < 0:
            raise Http404("User does not exist")
        else:
            transfers = Transfer.objects.filter(user_id=id)
        data = serializers.serialize("json", transfers)
        return HttpResponse(data, content_type="application/json")