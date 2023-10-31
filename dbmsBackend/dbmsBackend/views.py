from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from dbmsBackend import database

import json

@api_view(['GET'])
def hello_world(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# this is the GET method.
@api_view(['GET'])
def instructorPagination(request):
    storeProcedure = 'public.instructor__pagination'         # name of your DB function
    payload = json.dumps({"limit":10,"offset_id":1})         # payload structure
    
    data = database.db(storeProcedure,payload)               # call db function from database file

    context = {
        'data':data[0]
    }

    return Response(data)

@api_view(['GET'])
def teachesPagination(request):
    storeProcedure = 'public.teaches__pagination'
    payload = json.dumps({"limit":10,"offset_id":1})
    
    data = database.db(storeProcedure,payload)
    
    context = {
        'data':data[0]
    }

    return Response(data)



#  this function for  insert data to database by POST method .........................
@api_view(['POST'])
def instructorInsert(request):
    if request.method == "POST":
        storeProcedure = 'public.instructor__insert'       # name of your DB function
        
        # take your payload data from api json by request
        data = json.loads(json.dumps(request.data))
        name = data['name']
        dept_name = data['dept_name']
        salary = data['salary']

        payload = json.dumps({"name":name,"dept_name":dept_name, "salary":salary}) # payload structure
        # print(payload)          # debug

        data = database.db(storeProcedure,payload)      # call db function from database file

        context = {
            'data':data[0]
        }
        print(data)

        return Response(data)
