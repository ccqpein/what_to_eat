#! /usr/bin/env python
# -*- coding=utf-8 -*-

import _init
import random
# import click
import StoreData

def choice_module():
    dec = raw_input("吃什么？（输入1）录入新选择（输入2）查询现有选择（输入3）") or "None"
    dec = int(dec)
    return dec

def print_m(result):
    if result:
        print(result)
    else:
        print("貌似没有可供选择的店呢，新加点店面嗷")

def main(module):
    import StoreData
    
    if module == 1:
        try:
            i = random.randint(0, len(StoreData.store_list))
            result = "推荐 {0}！\n".format(StoreData.store_list[i][1].encode('utf-8'))
            if StoreData.store_list[i][2]:
                result += "地址为 {0}！".format(StoreData.store_list[i][2].encode('utf-8'))
            print_m(result)
        except IndexError:
            print_m(result)
            
    if module == 2:
        StoreData.input_store_name()
        result = "添加成功"
        print_m(result)

    if module == 3:
        if len(StoreData.store_list) == 0:
            blank_store()
        for i in range(len(StoreData.store_list)):
            result = '''编号：{0}  店名：{1}  地址：{2}\n'''  \
            .format(StoreData.all_store[i][0].encode('utf-8'),
                StoreData.all_store[i][1].encode('utf-8'),
                StoreData.all_store[i][2].encode('utf-8'))
            print_m(result)

    return result 

if __name__ == '__main__':
    main(choice_module())