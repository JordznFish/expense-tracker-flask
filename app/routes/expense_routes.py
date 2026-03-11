from flask import Blueprint

expense_bp = Blueprint("expense", __name__)

@expense_bp.route("/test")
def expense_route():
    return {"Message": "Expense route works perfectly"}