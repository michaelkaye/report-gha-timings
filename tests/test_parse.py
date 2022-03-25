import pytest

def test_success(report):
   result = report.parse({
     "action": "completed",
     "workflow_job": {
       "id": 2832853555,
       "run_id": 940463255,
       "status": "completed",
       "conclusion": "success",
       "started_at": "2021-06-15T19:00:00.000Z",
       "completed_at": "2021-06-15T19:02:00.123Z",
       "name": "first job"
     },
     "repository": {
        "full_name": "octo-org/example-workflow"
     }
   })


   assert result.repository == "octo-org/example-workflow"
   assert result.job_name == "first job"
   assert result.job_result == "success"
   assert result.job_run_time == 120

