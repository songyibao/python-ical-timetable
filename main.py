from data import AppleMaps, Course, Geo, School
import json
import re
from util import load_courses_from_csv
import datetime

# 品学楼地图 = AppleMaps("UESTC.ics")
# 立人楼A = Geo("电子科技大学清水河校区立人楼A区", 30.749454, 103.932191)
# 立人楼B = Geo("电子科技大学清水河校区立人楼B区", 30.748903, 103.931567)
# 定位信息的设置请参考 README.md

# 定位信息的设置请参考 README.md

courses = load_courses_from_csv("template.csv")
# 崂山校区上课时间
ls_time = [
    (8, 00),  # 上午第一节课时间为 8:30 至 9:15
    (9, 00),
    (10, 10),
    (11, 10),
    (13, 30),  # 下午第一节课时间为下午 1:30 至 2:20
    (14, 30),
    (15, 30),
    (16, 30),
    (17, 30),
    (18, 30),
    (19, 30),
    (20, 30)
]
# 西海岸校区上课时间
xha_time = [
    (8, 30),  # 上午第一节课时间为 8:30 至 9:15
    (9, 25),
    (10, 30),
    (11, 25),
    (13, 30),  # 下午第一节课时间为下午 1:30 至 2:20
    (14, 30),
    (15, 30),
    (16, 30),
    (17, 30),
    (18, 30),
    (19, 30),
    (20, 30)
]
school = School(
    duration=50,  # 每节课时间为 50 分钟
    timetable=xha_time,
    start=(2024, 2, 26),  # 2023 年 8 月 21 日是开学第一周星期一
    courses=courses
)

current_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
file_name = f"课表_{current_time}.ics"

with open(file_name, "w") as w:
    w.write(school.generate())
