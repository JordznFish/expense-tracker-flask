from app import create_app
from app.utils.db import get_db_connection
from contextlib import closing

app = create_app()

@app.route("/")
def home():
    return "hello"

if __name__ == "__main__":
    # conn = get_db_connection()
    try:
        with closing(get_db_connection()) as conn:
            if conn:
                print("Database connected successfully")
            else:
                print("Database connection failed!")
    except Exception as e:
        print(f"An error occurred: {e}")        
        
    app.run(debug=True, port=5000)