from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Reminder
from .serializers import ReminderSerializer

class ReminderCreateView(APIView):
    """View for creating, retrieving, updating, and deleting Reminder objects."""
    
    def get_queryset(self):
        """Retrieve all Reminder objects."""
        return Reminder.objects.all()
    
    def get(self, request, pk=-1):
        """Retrieve a list of all Reminder objects or a specific Reminder by ID.
        
        Args:
            request: HTTP request object.
            pk (int): Primary key of the Reminder object to retrieve. Default is -1.
        
        Returns:
            Response: Serialized data of Reminder objects with HTTP status code.
        
        Raises:
            Reminder.DoesNotExist: If Reminder with the specified ID does not exist.
        """
        queryset = self.get_queryset()
        serializer = ReminderSerializer(queryset, many=True)

        if pk == -1:
            return Response(serializer.data, status=status.HTTP_200_OK)

        try:
            reminder = queryset.get(id=pk)
            serializer = ReminderSerializer(reminder)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Reminder.DoesNotExist:
            return Response({"Error": "Reminder not found!"}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, format=None):
        """Create a new Reminder object.
        
        Args:
            request: HTTP request object containing data for creating the Reminder.
            format (str): Optional format of the request data.
        
        Returns:
            Response: Serialized data of the created Reminder object with HTTP status code.
        
        Raises:
            serializer.ValidationError: If request data is invalid.
        """
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        """Update an existing Reminder object.
        
        Args:
            request: HTTP request object containing updated data for the Reminder.
            pk (int): Primary key of the Reminder object to update.
            format (str): Optional format of the request data.
        
        Returns:
            Response: Serialized data of the updated Reminder object with HTTP status code.
        
        Raises:
            Reminder.DoesNotExist: If Reminder with the specified ID does not exist.
            serializer.ValidationError: If request data is invalid.
        """
        try:
            reminder = Reminder.objects.get(pk=pk)
            serializer = ReminderSerializer(reminder, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Reminder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        """Delete an existing Reminder object.
        
        Args:
            request: HTTP request object.
            pk (int): Primary key of the Reminder object to delete.
        
        Returns:
            Response: HTTP response indicating success or failure of the deletion.
        
        Raises:
            Reminder.DoesNotExist: If Reminder with the specified ID does not exist.
        """
        try:
            reminder = Reminder.objects.get(pk=pk)
            reminder.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Reminder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
