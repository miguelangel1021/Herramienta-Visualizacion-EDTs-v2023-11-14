class ApiError(Exception):
    code = 422


"""class NotFound(ApiError):
    code = 404
    description = "No se encontro informacion con los campos enviados."""



class DefaultError(ApiError):
    code = 406
    def __init__(self, description):
        self.description = description

