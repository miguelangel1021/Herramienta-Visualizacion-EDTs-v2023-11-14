
class ApiError(Exception):
    code = 422
    description = "Default_message"


"""class NotFound(ApiError):
    code = 404
    description = "No se encontro informacion con los campos enviados."""



class DefaultError(ApiError):
    code = 406
    def __init__(self, description):
        self.description = description


class IdNotInRequest(ApiError):
    code = 401
    description = "El Session Id no esta en el request"

class ExpiredSessionId(ApiError):
    code = 402
    description = "El Session-Id a expirado, ingrese nuevamente"
