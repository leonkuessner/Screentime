import json
import datetime

class GetData:
    def get_json_data(self):
        with open("Screentime/activities.json", "r") as f:
            data = json.load(f)
        print(self.sort_names(data))

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
                    # print((datetime.datetime.strptime(j_time["end_time"], "%Y-%m-%d %H:%M:%S")) - (datetime.datetime.strptime(j_time["start_time"], "%Y-%m-%d %H:%M:%S")))
                    # print(type(datetime.datetime.strptime(j_time["end_time"], "%Y-%m-%d %H:%M:%S")), "\n", type(datetime.datetime.strptime(j_time["start_time"], "%Y-%m-%d %H:%M:%S")))
                    total_time += ((datetime.datetime.strptime(j_time["end_time"], "%Y-%m-%d %H:%M:%S")) - (datetime.datetime.strptime(j_time["start_time"], "%Y-%m-%d %H:%M:%S"))).seconds
                    time_entries.append(
                        {
                            "start_time": data["activities"][i]["time_entry"][j][
                                "start_time"
                            ]
                        }
                    )
                    time_entries.append(
                        data["activities"][i]["time_entry"][j]["end_time"]
                    )

        # print(time_entries)
        return time_entries, total_time
    
    # def time_calculations(self, j_time):
        # time_spent = (datetime.datetime.strptime(j_time["end_time"], "%Y-%m-%d %H:%M:%S")) - (datetime.datetime.strptime(j_time["start_time"], "%Y-%m-%d %H:%M:%S"))

get_data = GetData()
sort_data = get_data.get_json_data()
