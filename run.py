from app.app import create_app
from waitress import serve

if __name__ == "__main__":
    app_instance = create_app()
    serve(app_instance, port=5000, host="0.0.0.0")
