from flask import render_template
from modules.admin import admin_bp

@admin_bp.route('/admin/complaints')
def complaints():
    return render_template('complaints.html'), 200
