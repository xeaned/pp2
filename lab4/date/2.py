from datetime import datetime, timedelta

today = datetime.now()
print("Today:", today.strftime("%x"))
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday.strftime("%x"))
print("Tomorrow:", tomorrow.strftime("%x"))