# Online Complaint Management System (OCMS)

Simple Flask-based OCMS with separate WEB and API apps.

## Quick start

1. Create & activate a venv
   - Windows:
     ```sh
     python -m venv venv
     venv\Scripts\activate
     ```
   - Unix:
     ```sh
     python -m venv venv
     source venv/bin/activate
     ```

2. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```

3. Run the WEB app
   ```sh
   python WEB/main.py
   ```
   - Main app: [`main.app`](WEB/main.py)
   - Config: [WEB/config-dev.toml](WEB/config-dev.toml)

4. Run the API app
   ```sh
   python API/main.py
   ```
   - Main app: [`API.main.app`](API/main.py)
   - Config: [API/config-dev.toml](API/config-dev.toml)

## Important files & symbols

- Requirements: [requirements.txt](requirements.txt)  
- DB / ORM:
  - [`model.config.db_session`](WEB/model/config.py)
  - DB models: [WEB/model/db.py](WEB/model/db.py)
  - DB init: [`model.config.init_db`](WEB/model/config.py)
- Mail:
  - Mail instance: [`mail`](WEB/mail_config.py)
  - Email view: [`modules.complaint.views.email.email_complaint`](WEB/modules/complaint/views/email.py)
  - Email form: [`modules.complaint.forms.models.EmailComplaintForm`](WEB/modules/complaint/forms/models.py)
- Templates (complaint email):
  - [WEB/modules/complaint/pages/email_form.html](WEB/modules/complaint/pages/email_form.html)
  - [WEB/modules/complaint/pages/email_.html](WEB/modules/complaint/pages/email_.html)
- Blueprints:
  - Login blueprint: [WEB/modules/login/__init__.py](WEB/modules/login/__init__.py)
  - Complaint blueprint: [WEB/modules/complaint/__init__.py](WEB/modules/complaint/__init__.py)

## Notes

- Mail settings are in [WEB/config-dev.toml](WEB/config-dev.toml) (MAIL_*). Ensure credentials are correct.
- Database URL is configured in [WEB/config-dev.toml](WEB/config-dev.toml) / [API/config-dev.toml](API/config-dev.toml).
- Templates for complaint email should be created at the paths above so the view [`modules.complaint.views.email.email_complaint`](WEB/modules/complaint/views/email.py) can render them.
