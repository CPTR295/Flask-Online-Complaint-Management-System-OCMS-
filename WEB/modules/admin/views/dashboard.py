from flask import render_template
from modules.admin import admin_bp

@admin_bp.route('/admin')
@admin_bp.route('/admin/dashboard')
def dashboard():
    return render_template('dashboard.html'), 200
