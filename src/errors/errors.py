
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
    description = "El id de la seson no existe, por favor intente de nuevo"

class ExpiredSessionId(ApiError):
    code = 402
    description = "Su sesión a expirado, ingrese nuevamente."
