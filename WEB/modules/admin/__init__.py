from flask import Blueprint

admin_bp = Blueprint('admin_bp',__name__,template_folder='pages',static_folder='resources',static_url_path='static')

# import view modules to register routes
import modules.admin.views.dashboard
import modules.admin.views.users
import modules.admin.views.complaints