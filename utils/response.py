from rest_framework.response import Response
from rest_framework import status


def success_response(data=None, message="Success", status_code=status.HTTP_200_OK):
    """성공 응답 템플릿"""
    response_data = {
        "success": True,
        "message": message,
        "data": data
    }
    return Response(response_data, status=status_code)


def error_response(message="Error", errors=None, status_code=status.HTTP_400_BAD_REQUEST):
    """실패 응답 템플릿"""
    response_data = {
        "success": False,
        "message": message,
        "errors": errors
    }
    return Response(response_data, status=status_code)


def created_response(data=None, message="Created successfully"):
    """생성 성공 응답"""
    return success_response(data, message, status.HTTP_201_CREATED)


def not_found_response(message="Not found"):
    """404 응답"""
    return error_response(message, status_code=status.HTTP_404_NOT_FOUND)


def unauthorized_response(message="Unauthorized"):
    """401 응답"""
    return error_response(message, status_code=status.HTTP_401_UNAUTHORIZED)
