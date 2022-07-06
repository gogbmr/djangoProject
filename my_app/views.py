from django.shortcuts import render
from .models import AllCourses, Details
# Create your views here.
from django.http import HttpResponse,Http404
from django.template import loader
def index(request):
    return HttpResponse('Hello, World! by deepak')

def Courses(request):
    ac=AllCourses.objects.all()
    template=loader.get_template('my_app/courses.html')
    context={'ac':ac,}
    return HttpResponse(template.render(context,request))

def details(request,course_id):
    try:
        course=AllCourses.objects.get(pk=course_id)
    except AllCourses.DoesNotExist:
        raise Http404("Course not available")
    return render(request,'my_app/details.html',{'coursename':course.coursename})