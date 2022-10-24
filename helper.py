import re
import datetime

from data import *


def search_course(subject, section='', instr=None, time_periods=None):
    if instr is None:
        instr = []
    if time_periods is None:
        time_periods = {}
    if subject == ' ':
        return {}
    subject_upper = subject_dict[subject]
    res = {}
    for course_name, each_course in data_dict.items():
        debug = 0
        if course_name == 'COMPSCI 101 - Introduction to Computer Science':
            debug = 1
        if course_name.split(' ')[0] == subject_upper:
            for class_name, each_class in each_course.items():
                break_flag = False
                if isinstance(each_class, dict):
                    if section != '' and each_class['section'] != section:
                        break
                    period_num = len(each_class['time'])
                    n_no_instr = []
                    for i in range(period_num):
                        period = []
                        if time_periods:
                            time_ok = False
                            for e in each_class['time'][i].split(' ')[1:][0::2]:
                                period.append(datetime.time(*(int(ee) for ee in e.split(':'))))
                            for day, p in time_periods.items():
                                if day in each_class['time'][i]:
                                    for exp_p in p:
                                        if period[0] >= exp_p[0] and period[1] <= exp_p[1]:
                                            time_ok = True
                                            break
                                        else:
                                            if debug:
                                                print(period,  exp_p, p)
                                    if time_ok:
                                        break
                            if not time_ok:
                                break_flag = True
                                break
                        if instr:
                            for instr_i in range(len(instr)):
                                n_no_instr.append(0)
                                if instr[instr_i] not in each_class['instr'][i]:
                                    n_no_instr[instr_i] += 1
                    if break_flag:
                        continue
                    if instr and sum(n_no_instr) == period_num * len(instr):
                        break
                    if course_name not in res:
                        res[course_name] = {}
                    res[course_name][class_name] = each_class
        if debug:
            debug = 0
    return res


def get_instr_names(course_data):
    instr_list = []
    for _, each_course in course_data.items():
        for _, each_class in each_course.items():
            for instrs in each_class['instr']:
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


def process_time_prompt(prompt):
    if prompt == '':
        return {}
    wkdays = ['Mo', 'Tu', 'We', 'Th']
    periods = {each: [] for each in wkdays}
    for each_period in prompt.split(','):
        if each_period.find('-') == -1:
            return -1
        times = each_period.split('-')
        period = []
        for each in times:
            if each.find(':') == -1:
                return -1
            try:
                h, m = (int(t) for t in each.split(':'))
                period.append(datetime.time(h, m))
            except ValueError:
                return -1
        for each in wkdays:
            periods[each].append(period)
    return periods