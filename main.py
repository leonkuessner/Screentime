from Screentime1 import *


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