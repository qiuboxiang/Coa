import os
import csv
import codecs

type = ("放小球", "擋小球", "殺球", "點扣", "挑球", "防守回挑", "長球", "平球", "小平球", "後場抽平球", "切球", "過渡切球", "推球",
         "撲球", "防守回抽", "勾球", "發短球", "發長球")
path = r"D:\CoachAI-Projects-main\CoachAI-Projects-main\ShuttleSet\set\Anders_ANTONSEN_Jonatan_CHRISTIE Indonesia_Masters_2020_QuarterFinals"
frame = 24
for dirc in os.listdir(path):
        dirc = os.path.join(path, dirc)
        if os.path.isdir(dirc):
            with codecs.open("annotation.txt", "w") as annotation:
                for f in os.listdir(dirc):
                    with open(os.path.join(dirc, f), "r", encoding="utf-8") as file:
                        reader = csv.DictReader(file)
                        first_line = reader[0]
                        player_location = {"A":"None", "B":"None"}

                        if first_line["player_location_y"] < ["opponent_location_y"]:
                            if first_line["player"] == "A":
                                player_location["A"] = "upper"
                                player_location["B"] = "lower"
                            else:
                                player_location["A"] = "upper"
                                player_location["B"] = "lower"
                        else:
                            if first_line["player"] == "B":
                                player_location["A"] = "upper"
                                player_location["B"] = "lower"
                            else:
                                player_location["A"] = "upper"
                                player_location["B"] = "lower"
                        for row in reader:
                            numbers = []
                            for word in row["time"].split():
                                if word.isdigit():
                                    numbers.append(word)
                            time = numbers[0] * 3600 + numbers[1] * 60 + numbers[2]
                            label = row["type"]









