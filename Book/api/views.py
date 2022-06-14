from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from library.models import Book
from .serializers import BookSerializer



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getBook(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addBook(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateBook(request, pk):
	book = Book.objects.get(id=pk)
	serializer = BookSerializer(instance=book, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteBook(request, pk):
	book = Book.objects.get(id=pk)
	book.delete()

	return Response('Item succsesfully delete!')

@api_view(['GET'])
def restricted(request):
    return Response(data='Only for logged in User', status=status.HTTP_200_OK)