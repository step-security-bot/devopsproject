"""
Unit tests for Flask application
"""

# Import sys module for modifying Python's runtime environment
import sys
# Import os module for interacting with the operating system
import os
# Import pytest for writing and running tests
import pytest

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# pylint: disable=C0413
# Import the Flask app instance from the main app file
from app import app

# pylint: disable=W0621
@pytest.fixture
def client():
    """Set up a test client for the app with setup and teardown logic."""
    print("\nSetting up the test client")
    with app.test_client() as client:
        yield client  # This is where the testing happens
    print("Tearing down the test client")

def test_home(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"version": "v0.0.1"}

def test_about(client):
    """Test the temperature route."""
    response = client.get('/temperature')
    assert response.status_code == 200

def test_non_existent_route(client):
    """Test for a non-existent route."""
    response = client.get('/non-existent')
    assert response.status_code == 404
