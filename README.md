# CPS847-A2-Practice
Code Cov: Create Branch, Commit, Merge  
Default port is 22  
Host is moon.scs.ryerson.ca  
Username and Password are moon Username and moons Password  
----------------------------------------------------
Slack bot
https://github.com/slackapi/python-slack-sdk/tree/main/tutorial
https://api.slack.com/start/building/bolt-python
https://github.com/miranska/cps847-w22/blob/main/1_slack_bot/app.py

pip install python-dotenv

import os
from dotenv import load_dotenv
from slack_bolt import App

 //Have a .env file with SLACK_BOT_TOKEN=<TOKEN>            
  
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)
  
if __name__ == "__main__":
  app.start(3000)
