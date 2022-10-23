import re

from data import *


def search_course(subject, section='', instr=None):
    if instr is None:
        instr = []
    if subject == ' ':
        return {}
    subject_upper = subjects[subject]
    res = {}
    for course_name, each_course in datadict.items():
        if course_name.split(' ')[0] == subject_upper:
            for class_name, each_class in each_course.items():
                if section != '' and each_class['section'] != section:
                    break
                period_num = len(each_class['time'])
                n_no_instr = []
                for i in range(period_num):
                    for instr_i in range(len(instr)):
                        n_no_instr.append(0)
                        if instr[instr_i] not in each_class['instructor'][i]:
                            n_no_instr[instr_i] += 1
                if instr != [] and sum(n_no_instr) == period_num * len(instr):
                    break
                if course_name not in res:
                    res[course_name] = {}
                res[course_name][class_name] = each_class
    return res


def get_instr_names(course_data):
    instr_list = []
    for _, each_course in course_data.items():
        for _, each_class in each_course.items():
            for instrs in each_class['instructor']:
                for each_instr in instrs.split(', '):
                    if each_instr not in instr_list:
                        instr_list.append(each_instr)
    return instr_list


def get_sections(course_data):
    section_list = []
    for _, each_course in course_data.items():
        for _, each_class in each_course.items():
            if each_class['section'] not in section_list:
                section_list.append(each_class['section'])
    if section_list:
        section_list = [''] + section_list
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
