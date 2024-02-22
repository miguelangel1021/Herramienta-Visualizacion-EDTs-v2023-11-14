class ApiError(Exception):
    code = 422
    description = "Default message"

"""class NotFound(ApiError):
    code = 404
    description = "No se encontro informacion con los campos enviados."

class ResourcesRequired(ApiError):
    code = 400
    description = "Hay algunos campos requeridos por favor valide."

class ResourcesAlreadyExist(ApiError):
    code = 412
    description = "El registro ya existe por favor valide."

class ExpiredInformation(ApiError):
    code = 401
    description = "La informacion que solicita ha expirado, considere autentificarse nuevamente."

class IncompleteRequest(ApiError):
    code = 403
    description = "No viene la informacion de autentificacion en la peticion."

class InvalidDate(ApiError):
    code = 412
    description = "Las fechas son invalidas."

class IncorrectId(ApiError):
    code = 400
    description = "El id del trayecto no esta en su debido formato."

class InvalidFlightId(ApiError):
    code = 400
    description = "No existe o es incorrecto el flightId."""


class IncompleteEstructure(ApiError):
    code = 400
    description = "La estructura no ha sido creada "

