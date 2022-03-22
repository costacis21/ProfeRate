from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpRequest,HttpResponse,HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from rate.models import Modules,Profs, ProfsManager,Ratings
import json

from django.contrib.auth.decorators import login_required



def getBadResponse():
    http_bad_response = HttpResponseBadRequest()
    http_bad_response['Content-Type'] = 'text/plain'
    return http_bad_response

@csrf_exempt
def HandleRegisterRequest(request):
    if request.method =='POST':
        data = request.POST
        newUsername = data.get('username')
        newPassword = data.get('password')
        if(len(newUsername)>0 and len(newPassword)>0):
            if not(User.objects.filter(username=newUsername).exists()):
                newUser = User.objects.create_user(newUsername,'',newPassword)
                response='New user %s has been created\n'% newUsername
            else:
                response='Username %s already exists\n' % newUsername
        else:
            response='Insufficient detailes provided, please try again\n'
    else:
        response = getBadResponse()

    
    return HttpResponse(response)


@csrf_exempt
def HandleLoginRequest(request):
   

    if request.method =='POST':
        data = request.POST
        newUsername = data.get('username')
        newPassword = data.get('password')
        if(len(newUsername)>0 and len(newPassword)>0):
            user = authenticate(username=newUsername, password = newPassword)
            if (user !=None):
                login(request,user)
                response='User %s has been logged in\n'% newUsername
            else:
                response='Wrong credentials\n'
        else:
            response='Insufficient detailes provided, please try again\n'
    else:
        response = getBadResponse()

    
    return HttpResponse(response)

@csrf_exempt
def HandleLogoutRequest(request):
    logout(request)

    return HttpResponse('User logged out\n')


@csrf_exempt
def HandleListRequest(request):
    data = serializers.serialize("json", Modules.objects.all(),fields=('code_by','full_name','semester','year','prof'),use_natural_foreign_keys=True)

    return HttpResponse(data)


@csrf_exempt
def HandleViewRequest(request):
    response=[]
    for professor in Profs.objects.all():
        ratings = Ratings.objects.filter(profs=professor)
        score=0
        i=1
        for i,rating in enumerate(ratings):
            score+=rating.rating
        score=score/(i+1)
        response.append({'name': professor.full_name, 'code': professor.name_code, 'rating': score})
    return HttpResponse(json.dumps(response))

# @login_required
@csrf_exempt
def HandleAverageRequest(request):
    response=[]
    exit=False
    if request.method =='POST':
        data = request.POST
        professor_id = data.get('professor_id')
        module_code = data.get('module_code')
        if(len(professor_id)>0 and len(module_code)>0):

            try:
                professor = Profs.objects.get(name_code=professor_id)
            except Profs.DoesNotExist:
                response="Couldn't find professor\t"
                exit=True
                
            try: 
                module=Modules.objects.filter(code_by=module_code)
            except Modules.DoesNotExist:
                response+="Couldn't find module"
                exit=True

            if(not exit):
                ratings = Ratings.objects.filter(profs=professor, modules__in=module)
                # ratings = ratings.filter(modules=module)
                # ratings.iterator
                score=0
                i=ratings.count()
                # i=0
                for rating in ratings:
                    score+=rating.rating
                if i!=0:
                    score=score/(i)

                    response.append(    {"name": professor.full_name    , 
                                        "name_code": professor.name_code, 
                                        "module_name": module[0].full_name,
                                        "module_code": module[0].code_by,
                                        "rating": score
                                        })
                else:
                    response="No ratings found"
                                
                # else:
                #     response="Couldn't find professor please try again"
        else:
            response='Insufficient detailes provided, please try again\n'
    else:
        response = getBadResponse()

    
    return HttpResponse(json.dumps(response))





# rate professor_id module_code year semester rating
@csrf_exempt
def HandleRateRequest(request):
    response=[]
    exit=False
    if request.method =='POST':
        data = request.POST
        professor_id = data.get('professor_id')
        module_code = data.get('module_code')
        year = data.get('year')
        semester = data.get('semester')
        rating = data.get('rating')



        if(len(professor_id)>0 and len(module_code)>0 and len(year)>0 and len(semester)>0 and len(rating)>0):

            try:
                professor = Profs.objects.get(name_code=professor_id)
            except Profs.DoesNotExist:
                response="Couldn't find professor\t"
                exit=True
                
            try: 
                module=Modules.objects.get(code_by=module_code,semester= semester, year=year)
            except Modules.DoesNotExist:
                response+="Couldn't find module"
                exit=True
            # print(professor.id)
            if(not exit):
                try:
                    newRating = Ratings(rating=rating,modules=module)
                    newRating.save()
                    newRating.profs.add(professor)
                    # newRating.rating.set(rating=rating)
                    newRating.save()
                    response="Rating succesfull"
                except:
                    response="something went wrong"
                  
        else:
            response='Insufficient detailes provided, please try again\n'
    else:
        response = getBadResponse()

    response+='\n'
    return HttpResponse(response)


# Create your views here.

