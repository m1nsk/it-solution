from django.http import HttpResponse, Http404
from .models import Message
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def get_messages(request):
    if request.method == 'GET':
        id = int(request.GET.get('last_id', -1))
        if id < 0:
            messages = Message.objects.filter(read_status=False)
        else:
            messages = Message.objects.filter(id__lte=id, read_status=False)
        data = serializers.serialize("json", messages)
        return HttpResponse(data, content_type="application/json")


@csrf_exempt
def mark_message(request):
    if request.method == 'GET':
        id = int(request.GET.get('id', -1))
        if id >= 0:
            try:
                message = Message.objects.get(id=id)
                message.read_status = True
                message.save()
                return HttpResponse("", content_type="application/json")
            except Message.DoesNotExist:
                raise Http404
        raise Http404

