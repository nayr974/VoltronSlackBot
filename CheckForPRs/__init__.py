import datetime
import logging
import json

import azure.functions as func
from utils import get_github_api, post_message


def main(mytimer: func.TimerRequest) -> None:
    api = get_github_api()
    results = api.search.issues_and_pull_requests(q='VOLT org:thinkific state:open label:"Ready for Review"', order='desc')

    links = ""
    for item in results["items"]:
        links += f"\n•\xa0<{item.pull_request.html_url}|{item.title[:75] + '...' if len(item.title) > 78 else item.title}>"

    post_message("#team-voltron", text="Reminder to review PRs.", blocks=[{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f":blob_wave: *{results.total_count} Voltron PR's are _Ready for Review_ today!*{links}"
			}
		}])
 