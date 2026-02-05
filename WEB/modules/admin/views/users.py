from flask import render_template
from modules.admin import admin_bp

@admin_bp.route('/admin/users')
def users():
    return render_template('users.html'), 200
