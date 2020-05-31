from datetime import datetime
import os


class Time_formatter:

 @staticmethod
 def get_timestamp(timestamp):
    if os.environ.get("HEROKU"):
        return timestamp
    else:
        return datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
