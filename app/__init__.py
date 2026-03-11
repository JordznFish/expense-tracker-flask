from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Routing (Import and register using BP)
    # Import
    from .routes.auth_routes import auth_bp
    from .routes.expense_routes import expense_bp
    
    #Register
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(expense_bp, url_prefix="/expense")
    
    return app