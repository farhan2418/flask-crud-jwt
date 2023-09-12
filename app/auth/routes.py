from flask import render_template, redirect, request, flash, url_for
from app.auth import bp
from app.extensions import HashPassword
from app.models.employee import Employee
import jwt
from datetime import datetime, timedelta 
from app.jwt_handlers import assign_access_refresh_tokens, unset_jwt

@bp.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        employee = Employee.query.filter_by(e_email=email).first()

        if employee and HashPassword.validate_hash(employee.password, password):
            # session['logged_in'] = True

            # token = jwt.encode({
            #     'email': employee.e_email,
            #     'expiration': str(datetime.utcnow() + timedelta(seconds=60))
            # }, Config.SECRET_KEY)
            
            # return redirect('/')
            flash('login successful', 'success')
            return assign_access_refresh_tokens(email, '/')
        
        else:
            flash('Invalid email or password', 'error')
            return redirect('/login')
    else:
        return render_template('login.html')
    
@bp.route('/logout')
def logout():
        return unset_jwt(), 302