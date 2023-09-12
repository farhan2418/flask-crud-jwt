from flask import render_template, redirect, session, make_response
from app.main import bp
from app.models.company import Company
from app.models.employee import Employee
from app.extensions import db
from flask_jwt_extended import jwt_required
from app.jwt_handlers import unset_jwt

@bp.route('/')
@jwt_required()
def index():
        
        employees = Employee.query.order_by(Employee.id.asc()).all()
        companies= Company.query.order_by(Company.date_opened.desc()).all()
        return render_template('index.html', companies = companies, employees = employees)

@bp.route('/delete/<int:id>')
@jwt_required(id)
def delete(id):
        emp_to_delete = Employee.query.get_or_404(id)
        try:
                db.session.delete(emp_to_delete)
                db.session.commit()
                return make_response(redirect('/', 302))
        except:
                return('There was an error deleting it')

