from Screentime1 import *
from activities_to_large import *
import json
import datetime
from time import sleep

# large_first_time = True
start_time = datetime.datetime.now()


with open("Screentime/activities.json", "r") as f:
    try:
        data = json.load(f)
        load_json = True
    except:
        load_json = False

with open("Screentime/large_json.json", "r") as f:
    try:
        data_large = json.load(f)
        large_first_time = False
    except:
        large_first_time = True

# try:
#     with open("Screentime/activities.json", "r") as f:
#         data = json.load(f)
#         load_json = True
#         # print(load_json, "load_json try")
# except:
#     load_json = False
#     # print("load_jon not work")
# try:
#     with open("Screentime/large_json.json", "r") as f:
#             data = json.load(f)
#             large_first_time = False
#             # print(large_first_time, "large try")
# except:
#     large_first_time = True

    # print("large not work")
first_time = True


def current_window():
    current_window = win32gui.GetForegroundWindow()
    active_window = win32gui.GetWindowText(current_window)
    return active_window

# i = 0
# while i < 10:
while True:
    active_window = current_window()
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)
    if current_time == "23:59:59" or current_time == "00:00:00" or current_time == "00:00:01":
        active_window = ""
        open("Screentime/activities.json", "w").close()
        load_json = False

    if active_window != previous_window:
        if not first_time:
            # print(first_time)
            end_time = datetime.datetime.now()
            print("________________________")
            print("window: ", active_window)
            print("start time: ", start_time)
            print("end time: ", end_time)
            print("________________________")
            # current_activity = Activity(active_window)
            activity_list = ActivityList([], previous_window, load_json)
            time_entry = activity_list.time_entries(start_time, end_time)
            activities = activity_list.data_from_json()

            get_data = GetData()
            sort_data = get_data.admin(large_first_time)
            load_json = True
            large_first_time = False
            previous_window = active_window
            start_time = datetime.datetime.now()
        first_time = False
    # i+=1
    sleep(2)
# from activities_to_large import *
# import json
# import datetime
# from time import sleep

# # large_first_time = True


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
        
#         try:
#             with open("Screentime/large_json.json", "r") as f:
#                 data = json.load(f)
#                 large_first_time = False
#         except:
#             large_first_time = True

#     if active_window != previous_window:
#         if first_time == False:
#             end_time = datetime.datetime.now()
#             previous_window = active_window
#             time_class = TimeEntries(start_time, end_time)
#             # current_activity = Activity(active_window)
#             activity_list = ActivityList([], active_window)
#             activities = activity_list.data_from_json()

#             get_data = GetData()
#             sort_data = get_data.admin(large_first_time)
#         first_time = False
#         start_time = datetime.datetime.now()
#     sleep(2)