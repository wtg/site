import re
import os

from requests import get
from flask import Flask, jsonify, render_template
from cachetools import TTLCache, cached

app = Flask(__name__)


def get_project_stubs():
    # list of tuples of human-readable name and GitHub repo slug
    basic_info = [
        ('Elections', 'elections'),
        ('Flagship', 'flagship_docs_4'),
        ('Petitions', 'petitions'),
        ('Senate Survey', 'senate-survey'),
        ('Student Government website', 'sg-site'),
        ('Shuttle Signups', 'shuttle-signups'),
        ('Shuttle Tracker', 'shuttletracker'),
        ('WebTech website', 'site')
    ]

    project_stubs = []
    for info in basic_info:
        project_stubs.append({
            'name': info[0],
            'slug': info[1]
        })

    return project_stubs


def get_open_issues_count_text(num_issues):
    if num_issues == 0:
        return 'No open issues'
    if num_issues == 1:
        return '1 open issue'
    return f'{num_issues} open issues'


def clean_commit_message_newlines(commit_message):
    """Remove single newlines but keep double newlines (empty lines).

    Avoids weird breaks in the middle of sentences on the webpage, because
    commit messages are usually broken every 80 chars, but this doesn't matter
    on the web."""

    return re.sub('(?<![\r\n])(\r?\n|\n?\r)(?![\r\n])', ' ', commit_message)


def get_projects():
    projects = []
    for project in get_project_stubs():

        # base repo info
        repo_url = 'https://api.github.com/repos/wtg/' + project['slug']
        project['repo'] = get_json_from_url(repo_url)

        project['repo']['open_issues_count_text'] = get_open_issues_count_text(project['repo']['open_issues_count'])

        # recent commits
        commits_url = repo_url + '/commits'
        project['commits'] = get_json_from_url(commits_url)[:5]

        for commit in project['commits']:
            commit['author']['name'] = get_json_from_url(commit['author']['url'])['name']
            commit['commit']['message'] = clean_commit_message_newlines(commit['commit']['message'])

        projects.append(project)

    return projects


@cached(cache=TTLCache(maxsize=128, ttl=60*60))
def get_json_from_url(url):
    if os.getenv('GITHUB_CLIENT_ID') and os.getenv('GITHUB_CLIENT_SECRET'):
        url += '?client_id=' + os.getenv('GITHUB_CLIENT_ID')
        url += '&client_secret=' + os.getenv('GITHUB_CLIENT_SECRET')
    return get(url).json()


@app.route('/')
def handle_index():
    projects = get_projects()
    return render_template('index.html', projects=projects)


if __name__ == '__main__':
    app.run(debug=True)
