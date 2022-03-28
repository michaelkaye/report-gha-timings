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



class Result:
   def __init__(self, job_id, repository, job_name, job_result, job_run_time, job_start_time):
       self.job_id = job_id
       self.repository = repository
       self.job_name = job_name
       self.job_result = job_result
       self.job_run_time = job_run_time
       self.job_start_time = job_start_time

   def __str__(self):
       return f"{self.job_id} {self.repository}/{self.job_name} {self.job_result} {self.job_start_time}->{self.job_run_time}"

class Report:
  def __init__(self):
     self.sqlite_db = None

  def init_app(self, app):
     self.sqlite_db = app.config['SQLITE3_DB']
     app.report = self
     self.init_db()
 
  def set_db(self, sqlite_db):
     self.sqlite_db = sqlite_db
  
  def get_time(self, time):
     FORMAT="%Y-%m-%dT%H:%M:%S.%fZ"
     ALT_FORMAT="%Y-%m-%dT%H:%M:%SZ"
     if time == None:
        return None
     try:
        return datetime.strptime(time, FORMAT)
     except:
        return datetime.strptime(time, ALT_FORMAT)
       
  def diff_times(self, start, end):
     if end == None:
        return None
     else:
        a = self.get_time(start)
        b = self.get_time(end)
        return (int)((b-a).total_seconds())
  
  def parse(self, json):
     if not 'workflow_job' in json:
         return None

     repository = json['repository']['full_name']
     job_id = json['workflow_job']['id']
     job_name = json['workflow_job']['name']
     job_result = json['workflow_job']['conclusion']
     job_start = json['workflow_job']['started_at']
     job_end = json['workflow_job']['completed_at']
     job_run_time = self.diff_times(job_start, job_end)
     return Result(job_id, repository, job_name, job_result, job_run_time, job_start)
  
  
  def write(self, result):
     print("deleting result ", result)
     conn = sqlite3.connect(self.sqlite_db)
     conn.execute("DELETE FROM history WHERE job_id = ?", (result.job_id,))
     conn.execute("INSERT INTO history (job_id, repository, job_name, job_result, job_run_time, job_start_time) VALUES (?,?,?,?,?,?)", (result.job_id, result.repository, result.job_name, result.job_result, result.job_run_time, result.job_start_time))
     conn.commit()


  def write_all(self, results):
     conn = sqlite3.connect(self.sqlite_db)
     for result in results:
       conn.execute("DELETE FROM history WHERE job_id = ?", (result.job_id,))
       conn.execute("INSERT INTO history (job_id, repository, job_name, job_result, job_run_time, job_start_time) VALUES (?,?,?,?,?,?)", (result.job_id, result.repository, result.job_name, result.job_result, result.job_run_time, result.job_start_time))
     
     conn.commit()
  
  def init_db(self):
    conn = sqlite3.connect(self.sqlite_db)
    conn.execute("""CREATE TABLE IF NOT EXISTS history (
      job_id INTEGER PRIMARY KEY NOT NULL,
      repository TEXT NOT NULL,
      job_name TEXT NOT NULL,
      job_result TEXT,
      job_run_time INTEGER,
      job_start_time TEXT NOT NULL
    )""")
    conn.close()

