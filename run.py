import os
from app.app import create_app
from waitress import serve

app_instance = create_app()

if __name__ == "__main__":
    print("Running with Waitress on port 5000...")
    serve(app_instance, host="0.0.0.0", port=5000)


