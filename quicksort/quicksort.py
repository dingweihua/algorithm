#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: 布丁(dingweihuaic@126.com)
#
# Created: 2018/1/2 下午2:13

import time
from random import randint


def quicksort1(alist):
    """
    快排算法1
    :param alist:
    :return:
    """
    if len(alist) <= 1:
        return alist
    pivot = alist[0]
    larger_list = []
    smaller_list = []
    pivot_list = []
    for i in alist:
        if i > pivot:
            larger_list.append(i)
        elif i < pivot:
            smaller_list.append(i)
        else:
            pivot_list.append(i)
    smaller_list = quicksort1(smaller_list)
    larger_list = quicksort1(larger_list)
    return smaller_list + pivot_list + larger_list


def quicksort2(alist):
    """
    快排算法2
    :param alist:
    :return:
    """
    if len(alist) <= 1:
        return alist
    pivot = alist[0]
    larger_list = []
    smaller_list = []
    for i in alist:
        if i > pivot:
            larger_list.append(i)
        else:
            smaller_list.append(i)
    smaller_list = quicksort1(smaller_list)
    larger_list = quicksort1(larger_list)
    return smaller_list + larger_list


def gen_list(smallest, largest, n):
    """
    生成无序列表
    :param smallest:
    :param largest:
    :param n:
    :return:
    """
    return [randint(smallest, largest) for i in range(n)]


if __name__ == '__main__':
    alist = gen_list(1, 100, 1000000)
    sms1 = time.time() * 1000
    sorted_list1 = quicksort1(alist)
    ems1 = time.time() * 1000
    sms2 = time.time() * 1000
    sorted_list2 = quicksort2(alist)
    ems2 = time.time() * 1000
    print(sorted_list1 == sorted_list2)
    print('ems1 - sms1 = {}'.format(ems1 - sms1))
    print('ems2 - sms2 = {}'.format(ems2 - sms2))
