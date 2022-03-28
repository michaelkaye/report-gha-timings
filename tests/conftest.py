import pytest
from flask import Flask
from app import create_app
from report import Report
from unittest.mock import Mock
import os

@pytest.fixture()
def app():
  with open('integration.db','a'):
    print("Working with integration.db")
  os.environ['SQLITE3_DB'] = 'integration.db'
  app = create_app()
  app.report.init_db()
  yield app
  os.remove('integration.db') 

@pytest.fixture()
def client(app):
    return app.test_client()
    
@pytest.fixture()
def report():
  with open('test.db','a'):
    print("Working with test.db")
  report = Report()
  report.set_db('test.db')
  yield report
  os.remove('test.db') 

