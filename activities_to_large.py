import json
import datetime

large_first_time = True

class GetData:
    def admin(self, large_first_time):
        # print(large_first_time, "large class")
        with open("Screentime/activities.json", "r") as f:
            data = json.load(f)

        if large_first_time == False:
            with open("Screentime/large_json.json", "r") as f:
                large_json = json.load(f)
        elif large_first_time == True:
            large_json = {"Date":[]}
        large_first_time = False
        
        large_json_data = self.serialize(large_json, data)

        with open("Screentime/large_json.json", "w") as json_file:
            json.dump(large_json_data, json_file, indent=4, sort_keys=True)
            

    def sort_names(self, data):
        name_list = []
        name_to_time = {}
        for i in range(len(data["activities"])):
            name_of_window = data["activities"][i]["name"]
            if name_of_window == "":
                continue

            split_name = (name_of_window.split("- "))[-1]
            name_list.append(split_name)

        for i in name_list:
            if i not in name_to_time:
                time_entries, time_seconds = self.time_for_names(data, i)
                name_to_time[i] = time_seconds
                # name_to_time[i] = self.time_for_names(data, i)

        return name_to_time

    def time_for_names(self, data, name):
        time_entries = []
        total_time = 0

        for i in range(len(data["activities"])):
            if name in data["activities"][i]["name"]:
                for j in range(len(data["activities"][i]["time_entry"])):
                    j_time = data["activities"][i]["time_entry"][j]
                    total_time += ((datetime.datetime.strptime(j_time["end_time"], "%Y-%m-%d %H:%M:%S")) - (datetime.datetime.strptime(j_time["start_time"], "%Y-%m-%d %H:%M:%S"))).seconds
                    time_entries.append(
                        {
                            "start_time": data["activities"][i]["time_entry"][j]["start_time"]
                        }
                    )
                    time_entries.append(
                        data["activities"][i]["time_entry"][j]["end_time"]
                    )

        return time_entries, total_time

    def serialize(self, large_json, data):
        date_exists = False

        today = (datetime.datetime.now()).strftime("%Y-%m-%d")

        for i in range(len(large_json["Date"])):
            if today in large_json["Date"][i]:
                date_exists = True
                large_json = self.add_time_to_existing(large_json, data, i, today)
                continue
        if date_exists == False:
            large_json["Date"].append({today:[self.sort_names(data)]})

        return large_json

    def add_time_to_existing(self, large_json, data, i, today):
        for j in self.sort_names(data):
            if j in large_json["Date"][i][today][0]:
                large_json["Date"][i][today][0][j] = (self.sort_names(data))[j]
                print(self.sort_names(data), self.sort_names(data)[j])
            else:
                large_json["Date"][i][today][0][j] = (self.sort_names(data))[j]
        return large_json


# get_data = GetData()
# sort_data = get_data.admin()

