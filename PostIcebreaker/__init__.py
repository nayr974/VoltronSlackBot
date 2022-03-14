import datetime
import logging
import random

import azure.functions as func
from utils import post_message, delete_message
from .icebreakers import ICEBREAKERS

def main(mytimer: func.TimerRequest) -> None:
    icebreaker = random.choice(ICEBREAKERS.splitlines())
    if random.choice([True,False,False,False]):
        post_message("#team-totoro", text="Icebreaker question!", blocks=[{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": f"<!subteam^S032EF67EUS> Getting to know you question! _{icebreaker}_ "
				}
			}])
	