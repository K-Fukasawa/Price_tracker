import pandas as pd
import datetime

timestamp = pd.Timestamp.now()
print("Timestamp:", timestamp.strftime("%Y-%m-%d, %H:%M"), timestamp.day_name())
