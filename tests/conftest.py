import pytest
from flask import Flask
from app import create_test_app
from report import Report
from unittest.mock import Mock

@pytest.fixture()
def app(mysql, report):

  app = create_test_app(mysql, report)
  return app

@pytest.fixture()
def client(app):
    return app.test_client()
    
@pytest.fixture()
def mysql():
   return Mock()

@pytest.fixture()
def report(mysql):
    return Report(mysql)

