from datetime import datetime, time as datetime_time, timedelta

event_duration = timedelta(hours=3, minutes=15)


date_time_str = "28 January 2023 06:20:00"

new_final_time = datetime.strptime(date_time_str, "%d %B %Y %H:%M:%S").time()

ini_time_for_now = datetime.now().time()

def time_diff(start, end):
    if isinstance(start, datetime_time): # convert to datetime
        assert isinstance(end, datetime_time)
        start, end = [datetime.combine(datetime.min, t) for t in [start, end]]
    if start <= end: # e.g., 10:33:26-11:15:49
        return end - start
    else: # end < start e.g., 23:55:00-00:25:00
        end += timedelta(1) # +day
        assert end > start
        return end - start

if __name__ == "__main__":
    time=time_diff(ini_time_for_now, new_final_time)
    print(str(time)[0:8])
