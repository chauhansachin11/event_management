from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .seriallizer import StudentSerializer


# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def studentApi(request,pk=None):
    if(request.method == 'GET'):
        if(pk != None):
            student = Student.objects.get(id=pk)
            serializer = StudentSerializer(student)
            return(Response(serializer.data))
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return(Response(serializer.data))

    if(request.method == 'POST'):
        serializer =  StudentSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return(Response({"msg":"Data created"}))
        return(Response(serializer.errors))

    if(request.method == 'PUT'):
        student = Student.objects.get(id=pk)
        serialiazer = StudentSerializer(student,data=request.data)
        if(serialiazer.is_valid()):
            serialiazer.save()
            return(Response({"msg": "Data Updated"}))
        return(Response(serialiazer.errors))

    if(request.method == 'PATCH'):
        student = Student.objects.get(id=pk)
        serialiazer = StudentSerializer(student, data=request.data, partial=True)
        if (serialiazer.is_valid()):
            serialiazer.save()
            return (Response({"msg": "Data Updated"}))
        return (Response(serialiazer.errors))

    if(request.method == 'DELETE'):
        student = Student.objects.get(id=pk)
        student.delete()
        return(Response({"msg": "Data Deleted"}))


