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


def test_real_one(report):
   result = report.parse({
      "action": "completed",
      "workflow_job": {
        "id": 5723661825,
        "run_id": 2053510255,
        "run_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/actions/runs/2053510255",
        "run_attempt": 1,
        "node_id": "CR_kwDOHD_Ers8AAAABVSgmAQ",
        "head_sha": "c119be913a4939cbed50b67c26567b9f52db9f68",
        "url": "https://api.github.com/repos/michaelkaye/report-gha-timings/actions/jobs/5723661825",
        "html_url": "https://github.com/michaelkaye/report-gha-timings/runs/5723661825?check_suite_focus=True",
        "status": "completed",
        "conclusion": "success",
        "started_at": "2022-03-28T16:13:57Z",
        "completed_at": "2022-03-28T16:14:24Z",
        "name": "build-and-push-image",
        "steps": [
          {
            "name": "Set up job",
            "status": "completed",
            "conclusion": "success",
            "number": 1,
            "started_at": "2022-03-28T16:13:56.000Z",
            "completed_at": "2022-03-28T16:13:58.000Z"
          },
          {
            "name": "Checkout repository",
            "status": "completed",
            "conclusion": "success",
            "number": 2,
            "started_at": "2022-03-28T16:13:58.000Z",
            "completed_at": "2022-03-28T16:13:58.000Z"
          },
          {
            "name": "Log in to the Container registry",
            "status": "completed",
            "conclusion": "success",
            "number": 3,
            "started_at": "2022-03-28T16:13:59.000Z",
            "completed_at": "2022-03-28T16:13:59.000Z"
          },
          {
            "name": "Extract metadata (tags, labels) for Docker",
            "status": "completed",
            "conclusion": "success",
            "number": 4,
            "started_at": "2022-03-28T16:13:59.000Z",
            "completed_at": "2022-03-28T16:13:59.000Z"
          },
          {
            "name": "Build and push Docker image",
            "status": "completed",
            "conclusion": "success",
            "number": 5,
            "started_at": "2022-03-28T16:13:59.000Z",
            "completed_at": "2022-03-28T16:14:23.000Z"
          },
          {
            "name": "Post Build and push Docker image",
            "status": "completed",
            "conclusion": "success",
            "number": 8,
            "started_at": "2022-03-28T16:14:23.000Z",
            "completed_at": "2022-03-28T16:14:23.000Z"
          },
          {
            "name": "Post Log in to the Container registry",
            "status": "completed",
            "conclusion": "success",
            "number": 9,
            "started_at": "2022-03-28T16:14:23.000Z",
            "completed_at": "2022-03-28T16:14:23.000Z"
          },
          {
            "name": "Post Checkout repository",
            "status": "completed",
            "conclusion": "success",
            "number": 10,
            "started_at": "2022-03-28T16:14:23.000Z",
            "completed_at": "2022-03-28T16:14:23.000Z"
          },
          {
            "name": "Complete job",
            "status": "completed",
            "conclusion": "success",
            "number": 11,
            "started_at": "2022-03-28T16:14:23.000Z",
            "completed_at": "2022-03-28T16:14:23.000Z"
          }
        ],
        "check_run_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/check-runs/5723661825",
        "labels": [
          "ubuntu-latest"
        ],
        "runner_id": 1,
        "runner_name": "Hosted Agent",
        "runner_group_id": 2,
        "runner_group_name": "GitHub Actions"
      },
      "repository": {
        "id": 473941166,
        "node_id": "R_kgDOHD_Erg",
        "name": "report-gha-timings",
        "full_name": "michaelkaye/report-gha-timings",
        "private": False,
        "owner": {
          "login": "michaelkaye",
          "id": 1917473,
          "node_id": "MDQ6VXNlcjE5MTc0NzM=",
          "avatar_url": "https://avatars.githubusercontent.com/u/1917473?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/michaelkaye",
          "html_url": "https://github.com/michaelkaye",
          "followers_url": "https://api.github.com/users/michaelkaye/followers",
          "following_url": "https://api.github.com/users/michaelkaye/following{/other_user}",
          "gists_url": "https://api.github.com/users/michaelkaye/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/michaelkaye/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/michaelkaye/subscriptions",
          "organizations_url": "https://api.github.com/users/michaelkaye/orgs",
          "repos_url": "https://api.github.com/users/michaelkaye/repos",
          "events_url": "https://api.github.com/users/michaelkaye/events{/privacy}",
          "received_events_url": "https://api.github.com/users/michaelkaye/received_events",
          "type": "User",
          "site_admin": False
        },
        "html_url": "https://github.com/michaelkaye/report-gha-timings",
        "description": "Collects data on github action timings and saves to database",
        "fork": False,
        "url": "https://api.github.com/repos/michaelkaye/report-gha-timings",
        "forks_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/forks",
        "keys_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/teams",
        "hooks_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/hooks",
        "issue_events_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/issues/events{/number}",
        "events_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/events",
        "assignees_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/assignees{/user}",
        "branches_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/branches{/branch}",
        "tags_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/tags",
        "blobs_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/languages",
        "stargazers_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/stargazers",
        "contributors_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/contributors",
        "subscribers_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/subscribers",
        "subscription_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/subscription",
        "commits_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/contents/{+path}",
        "compare_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/merges",
        "archive_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/downloads",
        "issues_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/issues{/number}",
        "pulls_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/labels{/name}",
        "releases_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/releases{/id}",
        "deployments_url": "https://api.github.com/repos/michaelkaye/report-gha-timings/deployments",
        "created_at": "2022-03-25T09:12:24Z",
        "updated_at": "2022-03-28T13:02:27Z",
        "pushed_at": "2022-03-28T16:13:42Z",
        "git_url": "git://github.com/michaelkaye/report-gha-timings.git",
        "ssh_url": "git@github.com:michaelkaye/report-gha-timings.git",
        "clone_url": "https://github.com/michaelkaye/report-gha-timings.git",
        "svn_url": "https://github.com/michaelkaye/report-gha-timings",
        "homepage": None,
        "size": 8,
        "stargazers_count": 0,
        "watchers_count": 0,
        "language": "Python",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": False,
        "forks_count": 0,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": None,
        "allow_forking": True,
        "is_template": False,
        "topics": [
    
        ],
        "visibility": "public",
        "forks": 0,
        "open_issues": 0,
        "watchers": 0,
        "default_branch": "main"
      },
      "sender": {
        "login": "michaelkaye",
        "id": 1917473,
        "node_id": "MDQ6VXNlcjE5MTc0NzM=",
        "avatar_url": "https://avatars.githubusercontent.com/u/1917473?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/michaelkaye",
        "html_url": "https://github.com/michaelkaye",
        "followers_url": "https://api.github.com/users/michaelkaye/followers",
        "following_url": "https://api.github.com/users/michaelkaye/following{/other_user}",
        "gists_url": "https://api.github.com/users/michaelkaye/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/michaelkaye/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/michaelkaye/subscriptions",
        "organizations_url": "https://api.github.com/users/michaelkaye/orgs",
        "repos_url": "https://api.github.com/users/michaelkaye/repos",
        "events_url": "https://api.github.com/users/michaelkaye/events{/privacy}",
        "received_events_url": "https://api.github.com/users/michaelkaye/received_events",
        "type": "User",
        "site_admin": False
      }
    })
   assert result.repository == "michaelkaye/report-gha-timings"
   assert result.job_name == "build-and-push-image"
   assert result.job_result == "success"
   assert result.job_run_time == 27
