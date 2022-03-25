#!/usr/bin/python3

import os
import click
import time
import re
from datetime import datetime
import requests
import json

import flask
from flask import Flask, render_template, request, Response
from flaskext.mysql import MySQL
from report import Report

def create_app():
  app = Flask(__name__)
  mysql = MySQL()
  report = Report(mysql)
  app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
  app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
  app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
  app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')
  mysql.init_app(app)
  report.init_app(app)
  return setup(app, mysql, report)

def create_test_app(mysql, report):
  app = Flask(__name__)
  mysql.init_app(app)
  report.init_app(app)
  return setup(app, mysql, report)

def setup(app, mysql, report):

  @app.route("/")
  def index_page():
    return render_template('index.j2.html')

  @app.route('/webhook/<path:path>', methods=['POST'])
  def handle_webhook(path):
    # POST request with body of JSON
    json = request.json
    result = report.parse(json)
    report.write(result)
    return "{}"
  
  @app.cli.command("initdb")
  def init_db():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE history (
      job_id INTEGER() NOT NULL,
      repository VARCHAR(255) NOT NULL,
      job_name VARCHAR(255) NOT NULL,
      job_result VARCHAR(80) NOT NULL,
      job_run_time INTEGER,
      job_start_time DATETIME NOT NULL,
      PRIMARY KEY (job_id),
      INDEX(repository, start_time)
    )""")
      
  
  @app.cli.command("import_history")
  @click.argument("since")
  @click.argument("repository")
  def import_history(repository, since):
    print(r"Reading {{ repository }} job history since {{ since }}")
    job_json = get_job_ids(repository, since)
    for job in job_json:
      report.write(report.parse(job))
    return


  return app

