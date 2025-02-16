from datetime import datetime, timedelta

today = datetime.now()
print("Today:", today.strftime("%x"))
five_days_ago = today - timedelta(days=5)
print("Five days ago:", five_days_ago.strftime("%x"))