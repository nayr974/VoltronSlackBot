import datetime
import logging
import random

import azure.functions as func
from utils import post_message, delete_message
from .gitjokes import JOKES

def main(mytimer: func.TimerRequest) -> None:
    joke = random.choice(JOKES.splitlines())
    post_message("#project-cb_react", text="Reminder to merge CB to master.", blocks=[{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"_{joke}_\n:merge: *REMINDER: It's time to merge CourseBuilder to master.* "
			}
		}])
 