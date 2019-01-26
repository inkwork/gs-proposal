## Github API Reference

### Commits

Commits by repository: https://developer.github.com/v3/repos/commits/#list-commits-on-a-repository

Data (including changes) from single commit: https://developer.github.com/v3/repos/commits/#get-a-single-commit

Tagged commits: https://developer.github.com/v3/repos/#list-tags


### Issue Reports

https://developer.github.com/v3/issues/#list-issues-for-a-repository

Note: every pull request is an issue, but not every issue is a pull request.  Issues endpoints return both issues and pull requests.  Identify pull requests ONLY with `pull_request` key

Issues Since Date (paginated):

```
curl -i "https://api.github.com/repos/chrissimpkins/Crunch/issues?state=closed&page=1&per_page=100&since=YYYY-MM-DDTHH:MM:SSZ"
```

Issues by Milestone, All (paginated)
```
curl -i "https://api.github.com/repos/chrissimpkins/Crunch/issues?milestone=[MILESTONE NUMBER]&state=all&page=1&per_page=100"
```

Issues by Milestone, Open only (paginated)
```
curl -i "https://api.github.com/repos/chrissimpkins/Crunch/issues?milestone=[MILESTONE NUMBER]&state=open&page=1&per_page=100"
```

Issues by Milestone, Closed only (paginated)
```
curl -i "https://api.github.com/repos/chrissimpkins/Crunch/issues?milestone=[MILESTONE NUMBER]&state=closed&page=1&per_page=100"
```

### Projects

Get Project Cards by Column: https://developer.github.com/v3/projects/columns/#get-a-project-column


### Statistics

Commit Activity grouped by week: https://developer.github.com/v3/repos/statistics/#get-the-last-year-of-commit-activity-data 

Number of additions/deletions per week: https://developer.github.com/v3/repos/statistics/#get-the-number-of-additions-and-deletions-per-week

