from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from ..serializers.ReviewSerializer import ReviewSerializer
from ..models.Review import Review


@csrf_exempt
def review_list(request):
    """
    List all code users, or create a new user.
    """
    if request.method == 'GET':
        user = Review.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = review_list(user, many=True, context=serializer_context)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def review_detail(request, pk):
    """
    Retrieve, update or delete a user.
    """
    try:
        skill = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ReviewSerializer(skill)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ReviewSerializer(skill, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        skill.delete()
        return HttpResponse(status=204)
