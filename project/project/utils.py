from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
def ExceptionHandling(func):

    @wraps(func)
    def inner(*args, **kwargs):

        try:

            return func(*args, **kwargs)
        
        except serializers.ValidationError as e:
        
            return Response({"error": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:

            return Response({"message": "something went wrong", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    return inner