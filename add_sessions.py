import pandas as pd
from datetime import date

# Load the csv as pandas DataFrame.
pd_stat = pd.read_csv("data.csv")

# Last record.
last_rec = len(pd_stat) - 1
last_rec_pd_cnt = pd_stat.loc[last_rec, "Sessions"]

# Get today's date.
today = date.today()
today_f = today.strftime("%Y-%m-%d")

def update_or_add_pomodoro_count():
    if pd_stat.loc[last_rec, "Date"] == today_f:
        # update exsisting entry.
        pd_stat.loc[last_rec, "Sessions"] = int(last_rec_pd_cnt) + 1
        pd_stat.to_csv("data.csv", index=False)
        print(f"Added 1 session to {today_f}.")
    else:
        # add new entry
        # adding a new entry involves creating a new series object and appending it to the csv
        new_entry = pd.Series(data=[today_f, 1], index=pd_stat.columns, name=last_rec+1)
        pd_stat.append(new_entry).to_csv("data.csv", index=False)
        print(f"{today_f} is not there. So I added it.")
