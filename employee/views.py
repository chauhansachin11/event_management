from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Employee, Department
from .serializer import EmployeeSerializer, DepartmentSerializer

# Class Based API View(using rest_framework.views import APIView)

class EmployeeAPI(APIView):
    def get(self,request,pk=None,format=None):
        if (pk != None):
            employee = Employee.objects.get(id=pk)
            serializer = EmployeeSerializer(employee)
            return (Response(serializer.data, status.HTTP_200_OK))
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return (Response(serializer.data, status.HTTP_200_OK))

    def post(self,request,fromat=None):
        serializer = EmployeeSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return (Response({"msg": "Data created"}, status.HTTP_201_CREATED))
        return (Response(serializer.errors, status.HTTP_400_BAD_REQUEST))

    def put(self,request,pk,format=None):
        employee = Employee.objects.get(id=pk)
        serialiazer = EmployeeSerializer(employee, data=request.data)
        if (serialiazer.is_valid()):
            serialiazer.save()
            return (Response({"msg": "Data Updated"}, status.HTTP_201_CREATED))
        return (Response(serialiazer.errors,status.HTTP_400_BAD_REQUEST))

    def patch(self,request,pk,format=None):
        employee = Employee.objects.get(id=pk)
        serialiazer = EmployeeSerializer(employee, data=request.data, partial=True)
        if (serialiazer.is_valid()):
            serialiazer.save()
            return (Response({"msg": "Data Updated"}, status.HTTP_201_CREATED))
        return (Response(serialiazer.errors,status.HTTP_400_BAD_REQUEST))

    def delete(self,request,pk,format=None):
        employee = Employee.objects.get(id=pk)
        employee.delete()
        return Response({"msg": "Data deleted"}, status=status.HTTP_200_OK)


class DepartmentAPI(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer