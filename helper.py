import re

from data import *


def search_by_subject(subject):
    subject_upper = subjects[subject]
    res = {}
    for each in datadict:
        if each.split(' ')[0] == subject_upper:
            res[each] = datadict[each]
    return res


def get_prof_names(course_data):
    prof_list = []
    for _, each_course in course_data.items():
        for _, each_class in each_course.items():
            for profs in each_class['instructor']:
                for each_prof in profs.split(', '):
                    if each_prof not in prof_list:
                        prof_list.append(each_prof)
    return prof_list


def get_sections(course_data):
    section_list = []
    for _, each_course in course_data.items():
        for _, each_class in each_course.items():
            if each_class['section'] not in section_list:
                section_list.append(each_class['section'])
    return section_list


def get_times(course_data):
    time_list = []
    for _, each_course in course_data.items():
        for _, each_class in each_course.items():
            for times in each_class['time']:
                for each_time in re.findall('([0-9]+:[0-9]+)', times):
                    if each_time not in time_list:
                        time_list.append(each_time)
    return time_list

print(get_times(datadict))