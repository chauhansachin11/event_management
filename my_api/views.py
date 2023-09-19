from rest_framework.response import Response
from rest_framework.decorators import api_view
from events.models import Item
from .serializer import ItemSerializers


@api_view(['GET'])
def getData(request):
    item = Item.objects.all()
    serializer = ItemSerializers(item, many=True)
    return(Response(serializer.data))

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return(Response(serializer.data))


