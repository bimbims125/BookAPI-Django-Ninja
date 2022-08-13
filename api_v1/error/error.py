from email import message
from ninja_extra.exceptions import APIException
from ninja_extra import api_controller, route, NinjaExtraAPI, status

class BadRequest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    message = "Data doesn't exist"