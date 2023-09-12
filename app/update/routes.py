from flask import redirect, request, render_template
from app.extensions import db
from app.update import bp
from app.models.employee import Employee
from flask_jwt_extended import jwt_required

@bp.route('/update/<int:id>', methods = ['POST', 'GET'])
# @jwt_required
def update(id):
    emp = Employee.query.get_or_404(id)
    if request.method == 'POST':
        emp.e_name = request.form.get('name')
        emp.e_email =request.form.get('email')
        
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'sorry, an error in updating the details'
    else:
        return render_template('update_emp.html', emp = emp)


