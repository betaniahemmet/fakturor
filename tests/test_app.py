import pytest
from fakturor.app.routes import main_blueprint
from fakturor.app.app import create_app

"""
GIVEN a flask application for testing
WHEN the '/' page is requested (GET)
THEN check if the response is valid

"""


def test_home_page_get():
    flask_app = create_app()
    flask_app.register_blueprint(main_blueprint, name='test_blueprint')

    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        
