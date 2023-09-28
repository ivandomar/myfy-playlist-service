from flask import redirect

def index():
    return redirect('/openapi/swagger')