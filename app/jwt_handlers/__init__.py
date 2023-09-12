from flask import make_response, redirect, flash
from flask_jwt_extended import (JWTManager, jwt_required, 
                                get_jwt_identity,
                                create_access_token, create_refresh_token, 
                                set_access_cookies, set_refresh_cookies, 
                                unset_jwt_cookies,unset_access_cookies)

jwt = JWTManager()

def assign_access_refresh_tokens(email,url):
    converted_email = str(email)
    access_token = create_access_token(identity=converted_email)
    refresh_token = create_refresh_token(identity=converted_email)
    
    resp = make_response(redirect(url, 302))
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)
   
    return resp

def unset_jwt():
    resp = make_response(redirect('/login', 302))
    unset_jwt_cookies(resp)
  
    return resp

@jwt.unauthorized_loader
def unauthorized_callback(callback):
    
    return redirect('/login', 302)

@jwt.invalid_token_loader
def invalid_token_callback(callback):
    resp = make_response(redirect('/login'))
    unset_jwt_cookies(resp)
    return resp, 302

@jwt.expired_token_loader
def expired_token_callback(self, callback):
    resp = make_response(redirect('/token/refresh'))
    unset_access_cookies(resp)
    return resp, 302

@jwt_required(refresh=True)
def refresh():
    email = get_jwt_identity()
    access_token = create_access_token(identity=str(email))
    resp = make_response(redirect('/', 302))
    set_access_cookies(resp, access_token)
    return resp 