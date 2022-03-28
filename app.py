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
import sqlite3
from report import Report

def create_app():
  app = Flask(__name__)
  app.config['SQLITE3_DB'] = os.environ.get('SQLITE3_DB')
  report = Report()  
  report.init_app(app)

  @app.route("/")
  def index_page():
    return render_template('index.j2.html')

  @app.route('/webhook/<path:path>', methods=['POST'])
  def handle_webhook(path):
    # POST request with body of JSON
    json = request.json
    result = report.parse(json)
    if result is not None:
      print(f"Writing data {result}")
      report.write(result)
      return '{"found":"valid result"}'
    else:
      return '{"found":"no workflow_job"}'
  
  @app.cli.command("initdb")
  def init_db():
    report.init_db()
      
  
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

