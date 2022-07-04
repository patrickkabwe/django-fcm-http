import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django_fcm_http_v1.fcmManager import FCMManager
from django_fcm_http_v1.models import Device


@csrf_exempt
def index(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        try:
            device = Device.objects.get(token=body.get('tokens'))
            device.send_message(
                data=body['data'], notification=body['notification'], tokens=body['tokens'])
            return HttpResponse("OK")
        except Exception as e:
            return HttpResponse(json.dumps(str(e)).encode('utf-8'), content_type='application/json')
