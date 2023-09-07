from data import AppleMaps, Course, Geo, School
import json
import re

# 品学楼地图 = AppleMaps("UESTC.ics")
# 立人楼A = Geo("电子科技大学清水河校区立人楼A区", 30.749454, 103.932191)
# 立人楼B = Geo("电子科技大学清水河校区立人楼B区", 30.748903, 103.931567)
# 定位信息的设置请参考 README.md

# 定位信息的设置请参考 README.md

# 课表数据可以用OUC+小程序抓包获取
# 西海岸课表数据
xha_kb_str = '[{"classes": [[{"name": "现代密码学", "num": 2, "weeks": ["5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"], "teacher": "林喜军", "classRoom": "信南B233", "day": 1, "begin": 2, "orgin": "5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21周", "py": 1}], [{"name": "自然辩证法概论", "num": 1, "weeks": ["11", "12", "13", "14", "15", "16", "17", "18"], "teacher": "杨晓斌", "classRoom": "信南B103", "day": 2, "begin": 1, "orgin": "11,12,13,14,15,16,17,18周", "py": 0}], "", [{"name": "高级操作系统及移动平台", "num": 2, "weeks": ["5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"], "teacher": "窦金凤", "classRoom": "信南B103", "day": 4, "begin": 2, "orgin": "5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21周", "py": 1}], [{"name": "软件安全", "num": 2, "weeks": ["5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"], "teacher": "曲海鹏", "classRoom": "信北A106", "day": 5, "begin": 1, "orgin": "5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21周", "py": 0}], "", ""], "time": "1 - 2节"}, {"classes": ["", [{"name": "新时代中国特色社会主义理论与实践", "num": 1, "weeks": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"], "teacher": "梁山", "classRoom": "信南B103", "day": 2, "begin": 3, "orgin": "2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18周", "py": 0}], "", "", "", "", ""], "time": "3 - 4节"}, {"classes": ["", [{"name": "最优化理论", "num": 2, "weeks": ["5", "6", "7", "8", "9", "10", "11", "12"], "teacher": "陈欣", "classRoom": "信南B235", "day": 2, "begin": 5, "orgin": "5,6,7,8,9,10,11,12周", "py": 0}], [{"name": "公共选修课", "num": 1, "weeks": ["5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"], "teacher": "郭金明", "classRoom": "北411/412(研讨)", "day": 3, "begin": 5, "orgin": "5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20周", "py": 0}], "", [{"name": "学术论文写作", "num": 2, "weeks": ["5", "6", "7", "8", "9", "10", "11", "12"], "teacher": "亓林", "classRoom": "信南B103", "day": 5, "begin": 5, "orgin": "5,6,7,8,9,10,11,12周", "py": 0}, {"name": "学术道德与规范", "num": 2, "weeks": ["13", "14", "15", "16", "17", "18", "19", "20", "21"], "teacher": "高峰", "classRoom": "南207/208", "day": 5, "begin": 5, "orgin": "13,14,15,16,17,18,19,20,21周", "py": 0}], "", ""], "time": "5 - 6节"}, {"classes": [[{"name": "人工智能与用户体验设计", "num": 1, "weeks": ["4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], "teacher": "袁鹏", "classRoom": "北415/416(研讨)", "day": 1, "begin": 7, "orgin": "4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19周", "py": 0}], "", "", "", "", "", ""], "time": "7 - 8节"}, {"classes": ["", "", "", "", "", "", ""], "time": "9 - 10节"}, {"classes": ["", "", "", "", "", "", ""], "time": "11 - 12节"}]'
# 崂山校区课表数据
ls_kb_str='[{"classes": [[{"name": "海洋遥感", "num": 2, "weeks": ["5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "21"], "teacher": "殷晓斌", "classRoom": "3205研", "day": 1, "begin": 1, "orgin": "5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21周", "py": 0}], "", [{"name": "研究生外国语(下)", "num": 2, "weeks": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"], "teacher": "秦晓星", "classRoom": "3203研", "day": 3, "begin": 1, "orgin": "2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18周", "py": 0}], "", [{"name": "海洋学概论", "num": 3, "weeks": ["5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"], "teacher": "高源", "classRoom": "3202研", "day": 5, "begin": 1, "orgin": "5,6,7,8,9,10,11,12,13,14,15,16,17周", "py": 0}], "", ""], "time": "1 - 2节"}, {"classes": ["", "", "", [{"name": "公共选修课", "num": 1, "weeks": ["5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"], "teacher": "何培英", "classRoom": "6313", "day": 4, "begin": 3, "orgin": "5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20周", "py": 0}], "", "", ""], "time": "3 - 4节"}, {"classes": ["", [{"name": "新时代中国特色社会主义理论与实践", "num": 1, "weeks": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"], "teacher": "张春晓", "classRoom": "4503", "day": 2, "begin": 5, "orgin": "2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18周", "py": 0}], "", "", [{"name": "学术道德与规范", "num": 3, "weeks": ["1", "2", "3", "4"], "teacher": "于方杰", "classRoom": "3101研", "day": 5, "begin": 5, "orgin": "1,2,3,4周", "py": 0}], "", ""], "time": "5 - 6节"}, {"classes": ["", [{"name": "自然辩证法概论", "num": 1, "weeks": ["11", "12", "13", "14", "15", "16", "17", "18"], "teacher": "韦雷雷", "classRoom": "4503", "day": 2, "begin": 7, "orgin": "11,12,13,14,15,16,17,18周", "py": 0}], "", "", "", "", ""], "time": "7 - 8节"}, {"classes": [[{"name": "数字地球与大数据地理学", "num": 2, "weeks": ["5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"], "teacher": "殷晓斌", "classRoom": "3304研", "day": 1, "begin": 10, "orgin": "5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21周", "py": 1}], [{"name": "海洋技术导论", "num": 3, "weeks": ["5", "6", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"], "teacher": "吴松华", "classRoom": "4501", "day": 2, "begin": 9, "orgin": "5,6,8,9,10,11,12,13,14,15,16,17周", "py": 0}, {"name": "学术论文写作", "num": 3, "weeks": ["1", "2", "3", "4"], "teacher": "高大治", "classRoom": "3202研", "day": 2, "begin": 9, "orgin": "1,2,3,4周", "py": 0}], "", [{"name": "学术论文写作", "num": 3, "weeks": ["1", "2", "3", "4"], "teacher": "高大治", "classRoom": "3202研", "day": 4, "begin": 9, "orgin": "1,2,3,4周", "py": 0}, {"name": "数字图像处理", "num": 2, "weeks": ["5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"], "teacher": "曾侃", "classRoom": "信南A516", "day": 4, "begin": 10, "orgin": "5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21周", "py": 1}], "", "", ""], "time": "9 - 10节"}, {"classes": ["", "", "", "", "", "", ""], "time": "11 - 12节"}]'

# 注意这里加载的课表数据
time_table = json.loads(ls_kb_str)
# 课程元数据，用于构造school对象
courses = []
pattern = re.compile(u'\d{1,2}')
# courses = [
#     Course("最优化理论与应用", "张三", "品学楼B107", 品学楼地图["品学楼B"], 1, Course.week(1, 13), [3, 4]),
#     # 张三老师的「最优化理论与应用」会在第 1 至 13 周的星期一第 3-4 节在 品学楼B107 教室上课
#     Course("新时代中国特色社会主义理论与实践", "李四", "立人楼B417", 立人楼B, 6, Course.week(1, 9) + [11], [7, 8]),
#     # 李四老师的「新时代中国特色社会主义理论与实践」会在第 1 至 9 周和第 11 周的的星期六第 7-8 节在 立人楼B417 教室上课
#     Course("雷达与电子对抗系统", "王五", "立人楼A417", 立人楼A, 2, Course.week(1, 9), Course.week(9, 11)),
#     # 王五老师的「雷达与电子对抗系统」会在第 1 至 9 周的星期二第 9-11 节在 立人楼A417 教室上课
#     Course("信号检测与估计", "赵六", "品学楼C411", 品学楼地图["品学楼C"], 4, Course.odd_week(1, 11), [5, 6]),
#     # 赵六老师的「信号检测与估计」会在第 1 至 11 的奇数周的星期四第 5-6 节在 品学楼C411 教室上课
# ]
for i in time_table:
    index_str = pattern.findall(i['time'])
    index = [int(x) for x in index_str]
    for j in i['classes']:
        for k in j:
            weeks_str = pattern.findall(k['orgin'])
            weeks = [int(i) for i in weeks_str]
            tmp = Course(k['name'], k['teacher'], k['classRoom'], None, k['day'], weeks,
                         [k['begin'], k['begin'] + k['num']])
            courses.append(tmp)
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
    timetable=ls_time,
    start=(2023, 8, 21),  # 2023 年 8 月 21 日是开学第一周星期一
    courses=courses
)

with open("课表.ics", "w") as w:
    w.write(school.generate())
