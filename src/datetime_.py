from datetime import datetime

print("NOW = ", datetime.now())
print("UTC = ", datetime.utcnow())
print("Date only = ", datetime.now().date())
print("Time only = ", datetime.now().time())
print(
    "Timestamp since epoch = ",
    datetime.now().timestamp(),
    int(datetime.now().timestamp()),
)

now = datetime.now()
print(f"Year = {now.year}, Month = {now.month}, Day = {now.day}")
print(
    f"Hour = {now.hour}, Minute = {now.minute}, Seconds = {now.second}, Milliseconds = {now.microsecond}"
)
