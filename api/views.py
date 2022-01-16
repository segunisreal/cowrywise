from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RandomUUID


class UUIDView(APIView):
    renderer_classes = (JSONRenderer,)
    
    def get(self, request):
        obj = RandomUUID.objects
        obj.create()
        data = {str(obj_.created_on): obj_.uuid for obj_ in obj.all()}
        data['doc'] = {
            'get_new_uuid': 'refresh this page',
            'admin_url': f"{request.scheme}://{request.get_host()}/admin",
            'username': 'admin',
            'password': 'admin',
            'NOTE': 'This response could be paginated, in case we have plenty of data to return.',
            'email': 'segunisreal.a@gmail.com',
            'phone': '+2348137933308',
            'cv_link': 'https://drive.google.com/file/d/1zx2ziWfstBR9LhTqV1HJOkoSnMX2FLMe/view?usp=sharing',
            'hail': 'Long Live Cowrywise!',
        }
        return Response(data)

