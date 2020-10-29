import win32gui
from time import time, sleep
import json
import datetime
from dateutil import parser

previous_window = ""

first_time = True
start_time = datetime.datetime.now()
load_json = False


class ActivityList:
    def __init__(self, activities, active_window):
        self.activities = activities
        self.active_window = active_window

    def data_from_json(self):
        added_to_existing = False

        data = {"activities": []}
        if load_json == True:
            with open("Screentime/activities.json", "r") as f:
                data = json.load(f)
            print(data)
            for i in range(len(data["activities"])):
                if data["activities"][i]["name"] == self.active_window:
                    # append only time becausse this window already exists in JSON file
                    data["activities"][i]["time_entry"].append(
                        time_class.current_time()
                    )
                    added_to_existing = True

        elif load_json == False:
            # JSON wont load if empty and if that is the case then this line will activate
            data["activities"].append(self.process_json(data))
            added_to_existing = True

        if added_to_existing == False:
            # If this window is the first instance in Json file, it must create a new dict
            data["activities"].append(self.process_json(data))

        first_time = False
        with open("Screentime/activities.json", "w") as json_file:
            json.dump(data, json_file, indent=4, sort_keys=True)
        return data

    def process_json(self, data):
        current_window_data = {
            "name": self.active_window,
            "time_entry": [time_class.current_time()],
        }
        # print(current_window_data)
        return current_window_data


# class Activities:
#     def __init__(self, current_window):
#         self.current_window = current_window

#     def process_previous_window(self, data, previous_window):  # Data is return_list
#         end_date = datetime.datetime.now()
#         print(data["end_time"])

#     # def process_new_window(self, new_window):
#     # start_time = datetime.datetime.now()
#     def add_to_list(self, new_window, data):
#         # if new_window["name"] in data:
#         print(data)
#         # data["time_entries"].append(new_window["time_entries"])
#         # else:
#         #   data["activities"].append(new_window)
#         # print(data)
#         # return data


class TimeEntries:
    def __init__(self, start_time_dt, end_time_dt):
        self.start_time_dt = start_time
        self.end_time_dt = end_time_dt
        self.start_time = self.start_time_dt.strftime("%Y-%m-%d %H:%M:%S")
        self.end_time = self.end_time_dt.strftime("%Y-%m-%d %H:%M:%S")
        self.days = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def current_time(self):
        # time = datetime.datetime.now()

        return_list = self.specific_times(start_time, end_time)
        return return_list

    def specific_times(self, start_time, end_time):
        total_time = end_time - start_time
        self.days, self.seconds = total_time.days, total_time.seconds
        self.hours = self.days * 24 + self.seconds // 3600
        self.minutes = (self.seconds % 3600) // 60
        self.seconds = self.seconds % 60

        return_list = {
            "start_time": self.start_time,
            "end_time": self.end_time,
            "days": self.days,
            "hours": self.hours,
            "minutes": self.minutes,
            "seconds": self.seconds,
        }
        return return_list


# class DataToJson:
#   def __init__(self, data):
#   self.data = data


def current_window():
    current_window = win32gui.GetForegroundWindow()
    active_window = win32gui.GetWindowText(current_window)
    return active_window


i = 0
while i < 5:
    # while True:
    active_window = current_window()
    if load_json == False:
        try:
            with open("Screentime/activities.json", "r") as f:
                data = json.load(f)
                load_json = True
        except:
            load_json = False

    print(load_json)
    if active_window != previous_window:
        if first_time == False:
            end_time = datetime.datetime.now()
            time_class = TimeEntries(start_time, end_time)
            print(active_window)
            previous_window = active_window
            # current_activity = Activity(active_window)
            activity_list = ActivityList([], active_window)
            activities = activity_list.data_from_json()
        first_time = False
        start_time = datetime.datetime.now()
        i += 1
    sleep(2)
