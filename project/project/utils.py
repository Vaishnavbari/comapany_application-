from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from application.models import application_access
from company.models import company_provider, company
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


def CheckCompanyAccess(user_id=None, company_id=None, company_name=None):
    
    if user_id and company_id:
        user_access = application_access.objects.filter(user_id=user_id ,application_access=company_id)
        return user_access
    
    if company_name :
        check_company = company.objects.filter(legan_name=company_name).first()
        return check_company
    
