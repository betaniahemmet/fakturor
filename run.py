from app.app import create_app
from waitress import serve

if __name__ == "__main__":
    app_instance = create_app()
    if app_instance is None:
        print("Error: App instance is None")
    else:
        print("App created successfully")
    serve(app_instance, port=5000, host="0.0.0.0")
