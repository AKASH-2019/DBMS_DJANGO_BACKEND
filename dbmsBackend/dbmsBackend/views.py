from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from dbmsBackend import database

import json

@api_view(['GET'])
def hello_world(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@api_view(['GET'])
def instructor_pagination(request):

    # storeProcedure = 'pet.product__pagination_by_pet'
    # payload = json.dumps({"slug":"dog","limit":10,"offset_id":1})
    storeProcedure = 'public.instructor__pagination'
    payload = json.dumps({"limit":10,"offset_id":1})
    
    data = database.db(storeProcedure,payload)
    

    context = {
        'data':data[0]
    }

    return Response(data)
    # return render(request, 'hello_world/hello_world.html', context)


@api_view(['GET'])
def teaches_pagination(request):

    # storeProcedure = 'pet.product__pagination_by_pet'
    # payload = json.dumps({"slug":"dog","limit":10,"offset_id":1})
    storeProcedure = 'public.teaches__pagination'
    payload = json.dumps({"limit":10,"offset_id":1})
    
    data = database.db(storeProcedure,payload)
    

    context = {
        'data':data[0]
    }

    return Response(data)

