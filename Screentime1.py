import win32gui
from time import time, sleep
import json
import datetime
from dateutil import parser
# from activities_to_large import *
# from main import *

previous_window = ""

# first_time = True
# start_time = datetime.datetime.now()



class ActivityList:
    def __init__(self, activities, active_window, load_json):
        self.load_json = load_json
        self.activities = activities
        self.active_window = active_window

    def data_from_json(self):
        added_to_existing = False
        # print(self.load_json, "load_json class")

        data = {"activities": []}
        if self.load_json == True:
            with open("Screentime/activities.json", "r") as f:
                data = json.load(f)
            for i in range(len(data["activities"])):
                if data["activities"][i]["name"] == self.active_window:
                    # append only time becausse this window already exists in JSON file
                    data["activities"][i]["time_entry"].append(
                        self.specific_times()
                    )
                    added_to_existing = True
                    

        elif self.load_json == False:
            # JSON wont load if empty and if that is the case then this line will activate
            data["activities"].append(self.process_json(data))
            added_to_existing = True
            self.load_json = True

        if added_to_existing == False:
            # If this window is the first instance in Json file, it must create a new dict
            data["activities"].append(self.process_json(data))

        # first_time = False
        with open("Screentime/activities.json", "w") as json_file:
            json.dump(data, json_file, indent=4, sort_keys=True)
        return data

    def process_json(self, data):
        current_window_data = {
            "name": self.active_window,
            "time_entry": [self.specific_times()],
        }
        return current_window_data

    def time_entries(self, start_time_dt, end_time_dt):
        self.start_time_dt = start_time_dt
        self.end_time_dt = end_time_dt
        self.start_time = self.start_time_dt.strftime("%Y-%m-%d %H:%M:%S")
        self.end_time = self.end_time_dt.strftime("%Y-%m-%d %H:%M:%S")
        self.days = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    # def current_time(self):
    #     # time = datetime.datetime.now()

    #     return_list = self.specific_times(start_time, end_time)
    #     return return_list

    def specific_times(self):
        total_time = self.end_time_dt - self.start_time_dt
        print(total_time)
        self.days, self.seconds = total_time.days, total_time.seconds
        print(self.days)
        self.hours = self.days * 24 + self.seconds // 3600
        print(self.hours)
        self.minutes = (self.seconds % 3600) // 60
        print(self.minutes)
        self.seconds = self.seconds % 60
        print(self.seconds)

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


# def current_window():
#     current_window = win32gui.GetForegroundWindow()
#     active_window = win32gui.GetWindowText(current_window)
#     return active_window

# while True:
#     # while True:
#     active_window = current_window()
#     if load_json == False:
#         try:
#             with open("Screentime/activities.json", "r") as f:
#                 data = json.load(f)
#                 load_json = True
#         except:
#             load_json = False

#     print(load_json)
#     if active_window != previous_window:
#         if first_time == False:
#             end_time = datetime.datetime.now()
#             previous_window = active_window
#             # current_activity = Activity(active_window)
#             activity_list = ActivityList([], active_window)
#             time_class = activity_list.time_entries(start_time, end_time)
#             activities = activity_list.data_from_json()

#             # get_data = GetData()
#             # sort_data = get_data.admin()
#         first_time = False
#         start_time = datetime.datetime.now()
#     sleep(2)
# import win32gui
# from time import time, sleep
# import json
# import datetime
# from dateutil import parser
# # from activities_to_large import *
# # from main import *

# previous_window = ""

# first_time = True
# start_time = datetime.datetime.now()
# load_json = False


# class ActivityList:
#     def __init__(self, activities, active_window):
#         self.activities = activities
#         self.active_window = active_window

#     def data_from_json(self):
#         added_to_existing = False
#         print(load_json, "Load Json")

#         data = {"activities": []}
#         if load_json == True:
#             with open("Screentime/activities.json", "r") as f:
#                 data = json.load(f)
#             for i in range(len(data["activities"])):
#                 if data["activities"][i]["name"] == self.active_window:
#                     # append only time becausse this window already exists in JSON file
#                     data["activities"][i]["time_entry"].append(
#                         TimeEntries.specific_times
#                     )
#                     added_to_existing = True

#         elif load_json == False:
#             # JSON wont load if empty and if that is the case then this line will activate
#             data["activities"].append(self.process_json(data))
#             added_to_existing = True

#         if added_to_existing == False:
#             # If this window is the first instance in Json file, it must create a new dict
#             data["activities"].append(self.process_json(data))

#         first_time = False
#         with open("Screentime/activities.json", "w") as json_file:
#             json.dump(data, json_file, indent=4, sort_keys=True)
#         return data

#     def process_json(self, data):
#         current_window_data = {
#             "name": self.active_window,
#             "time_entry": [TimeEntries.specific_times],
#         }
#         return current_window_data

# class TimeEntries:
#     def __init__(self, start_time_dt, end_time_dt):
#         self.start_time_dt = start_time
#         self.end_time_dt = end_time_dt
#         self.start_time = self.start_time_dt.strftime("%Y-%m-%d %H:%M:%S")
#         self.end_time = self.end_time_dt.strftime("%Y-%m-%d %H:%M:%S")
#         self.days = 0
#         self.hours = 0
#         self.minutes = 0
#         self.seconds = 0

#     def specific_times(self):
#         total_time = end_time - start_time
#         print(total_time)
#         self.days, self.seconds = total_time.days, total_time.seconds
#         print(self.days)
#         self.hours = self.days * 24 + self.seconds // 3600
#         print(self.hours)
#         self.minutes = (self.seconds % 3600) // 60
#         print(self.minutes)
#         self.seconds = self.seconds % 60
#         print(self.seconds)

#         return_list = {
#             "start_time": self.start_time,
#             "end_time": self.end_time,
#             "days": self.days,
#             "hours": self.hours,
#             "minutes": self.minutes,
#             "seconds": self.seconds,
#         }
#         return return_list


# # class DataToJson:
# #   def __init__(self, data):
# #   self.data = data


# # def current_window():
# #     current_window = win32gui.GetForegroundWindow()
# #     active_window = win32gui.GetWindowText(current_window)
# #     return active_window

# # while True:
# #     # while True:
# #     active_window = current_window()
# #     if load_json == False:
# #         try:
# #             with open("Screentime/activities.json", "r") as f:
# #                 data = json.load(f)
# #                 load_json = True
# #         except:
# #             load_json = False

# #     print(load_json)
# #     if active_window != previous_window:
# #         if first_time == False:
# #             end_time = datetime.datetime.now()
# #             time_class = TimeEntries(start_time, end_time)
# #             previous_window = active_window
# #             # current_activity = Activity(active_window)
# #             activity_list = ActivityList([], active_window)
# #             activities = activity_list.data_from_json()

# #             # get_data = GetData()
# #             # sort_data = get_data.admin()
# #         first_time = False
# #         start_time = datetime.datetime.now()
# #     sleep(2)
