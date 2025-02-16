from datetime import datetime

date1_str = input("Enter the 1st date (YYYY-MM-DD HH:MM:SS): ")
date2_str = input("Enter the 2nd date (YYYY-MM-DD HH:MM:SS): ")

format = "%Y-%m-%d %H:%M:%S"

date1 = datetime.strptime(date1_str, format)
date2 = datetime.strptime(date2_str, format)

difference = abs(date1 - date2)
seconds = difference.total_seconds()
print(f"Difference in seconds: {seconds}")