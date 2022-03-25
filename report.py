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



class Result:
   def __init__(self, job_id, repository, job_name, job_result, job_run_time, job_start_time):
       self.job_id = job_id
       self.repository = repository
       self.job_name = job_name
       self.job_result = job_result
       self.job_run_time = job_run_time
       self.job_start_time = job_start_time

class Report:


  def __init__(self, mysql):
    self.mysql = mysql
  
  def init_app(self, app):
     return 
  
  def diff_times(self, start, end):
     FORMAT="%Y-%m-%dT%H:%M:%S.%fZ"
     if end == None:
        return None
     else:
        a = datetime.strptime(start, FORMAT)
        b = datetime.strptime(end, FORMAT)
        return (int)((b-a).total_seconds())
  
  def parse(self, json):
     repository = json['repository']['full_name']
     job_id = json['workflow_job']['id']
     job_name = json['workflow_job']['name']
     job_result = json['workflow_job']['conclusion']
     job_start = json['workflow_job']['started_at']
     job_end = json['workflow_job']['completed_at']
     job_run_time = self.diff_times(job_start, job_end)
     return Result(job_id, repository, job_name, job_result, job_run_time, job_start)
  
  
  def write(self, result):
     conn = self.mysql.connect()
     cursor = conn.cursor()
     cursor.execute("DELETE FROM history WHERE job_id = ?", result.job_id)
     cursor.execute("INSERT INTO history (job_id, repository, job_name, job_result, job_run_time, job_start_time) VALUES (?,?,?,?,?,?)", result.job_id, result.repository, result.job_name, result.job_result, result.job_run_time, result.job_start_time)
  

