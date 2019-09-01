from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from ..serializers.SkillSerializer import SkillSerializer
from ..models.Skill import Skill


@csrf_exempt
def skill_list(request):
    """
    List all code users, or create a new user.
    """
    if request.method == 'GET':
        user = Skill.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = SkillSerializer(user, many=True, context=serializer_context)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SkillSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def skill_list_by_group(request, skills_group_id):
    """
    List all code users, or create a new user.
    """
    if request.method == 'GET':
        try:
            skills = Skill.objects.filter(skills_group_id=skills_group_id)
            serializer_context = {
                'request': request,
            }
            serializer = SkillSerializer(skills, many=True, context=serializer_context)
            return JsonResponse(serializer.data, safe=False)
        except:
            return HttpResponse(status=404)

@csrf_exempt
def skill_detail(request, pk):
    """
    Retrieve, update or delete a user.
    """
    try:
        skill = Skill.objects.get(pk=pk)
    except Skill.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SkillSerializer(skill)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SkillSerializer(skill, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        skill.delete()
        return HttpResponse(status=204)
