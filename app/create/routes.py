from flask import render_template, request, redirect
from app.create import bp
from app.models.company import Company
from app.models.employee import Employee
from app.extensions import db, HashPassword
from flask_jwt_extended import jwt_required

@bp.route('/create_employee',methods = ['POST', 'GET'] )
# @jwt_required()
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = HashPassword.generate_hash(password)
        company_name = request.form.get('company')
        company = Company.query.filter_by(c_name = company_name).first()
        emp_task = Employee(e_name = name, e_email = email, password = hashed_password, company = company)

        try:
            db.session.add(emp_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'sorry an error occured!'
        
    else:
        companies= Company.query.order_by(Company.date_opened).all()

        return render_template('create_emp.html', companies = companies)

