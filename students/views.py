from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .seriallizer import StudentSerializer


# Create your views here.
@api_view(['GET'])
def studentList(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student,many=True)
    return(Response(serializer.data))

@api_view(['GET'])
def studentDetails(request,pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, many=False)
    return (Response(serializer.data))

@api_view(['POST'])
def studentCreate(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return(Response(serializer.data))


@api_view(['POST'])
def studentUpdate(request,pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)
    if(serializer.is_valid()):
        serializer.save()
    return(Response(serializer.data))

@api_view(['DELETE'])
def studentDelete(request,pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return(Response("Student Deleted !"))



