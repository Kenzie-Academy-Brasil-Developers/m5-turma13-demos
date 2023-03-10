def generic_error_handler(error: Exception):
    return {"detail": error.message}, error.status_code
