# This file is the entry point to the server.
import sys
import os
from bottle import run, route, TEMPLATE_PATH, redirect, request, template

# Prevents python from generating cache files
sys.dont_write_bytecode = True

# Appends the path to your interfaces directory to Bottle's template search path
interfaces_dir = os.path.join(os.getcwd(), 'interfaces')
TEMPLATE_PATH.append(interfaces_dir)

'''
# default route to login page
@route("/")
def redirect_to_login_page():
    return redirect("/login")

# login page route
@route("/login")
def show_login_page():
    return template("login", error_message=None, has_error=None)

# login page logic for error handling
@route("/login", method="post")
def handle_login():
    a = logic.handle_login(request.forms.get('username'), request.forms.get('password'))
    if a[0]:
        return redirect("/reviews")
    else:
        return template("login", error_message=a[1], has_error=a[2])

# register page route
@route("/register")
def show_register_page():
    return template("register", error_message=None, has_error=None)

# login page logic for error handling 
@route("/register", method="post")
def handle_register():
    a = logic.handle_register(request.forms.get('wanted_username'), request.forms.get('wanted_password'))
    if a[0]:
        return template("login", error_message=a[1], has_error=a[2])
    else:
        return template("register", error_message=a[1], has_error=a[2])

# review page route
@route("/reviews")
def show_reviews():
    return template("review_list")

# logout page route
@route("/logout")
def logout():
    logic.handle_logout()
    return redirect("/login")
'''

# server information
hostname = 'localhost'
port = 8080

# Sets up the database
# db.setup()

if __name__ == "__main__":
    run(host=hostname, port=port, debug=True)
