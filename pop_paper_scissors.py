"""
分歧终端机
The Conflict Resolution Terminal

created_time = 20190324.5.46 pm - 7 pm

created_by = tzh
"""

import random
import time


USER_NAME = ['哥哥', '艳艳']
RULES = ['剪刀', '石头', '布']
WIN_LIST = [["布", "石头"], ["石头", "剪刀"], ["剪刀", "布"]]


class Terminator(object):
    """终结争端机类"""
    def __init__(self):
        print("分歧终端机启用中...\n")
        time.sleep(1)

    def start(self):
        """介绍选手"""
        user_list = USER_NAME
        rule_list = RULES
        random.shuffle(user_list)
        user_1 = user_list[0]
        user_2 = user_list[1]
        print("欢迎第一位选手：{}！".format(user_1))
        time.sleep(1)
        print("欢迎第二位选手：{}！".format(user_2))
        time.sleep(1)
        result_1 = random.choice(rule_list)
        result_2 = random.choice(rule_list)
        print("计算中...\n")
        time.sleep(0.5)
        print("{} 出了 {} ！".format(user_1, result_1))
        time.sleep(1)
        print("{} 出了 {} ！".format(user_2, result_2))
        result_list = [[user_1, result_1], [user_2, result_2]]
        return result_list

    def computation(self, result_list):
        """计算"""
        time.sleep(2)
        user_1_result = result_list[0][1]
        user_2_result = result_list[1][1]
        if user_1_result == user_2_result:
            print("Oops, 双方平手！再来一次！！！")
            return 0
        else:
            for i in WIN_LIST:
                if user_1_result == i[0]:
                    if user_2_result not in i:
                        print("\n胜出的是！！！  {}   !!!\n".format(result_list[1][0]))
                        return 1
                    elif user_2_result == i[1]:
                        print("\n胜出的是！！！  {}   !!!\n".format(result_list[0][0]))
                        return 1
                    else:
                        return 0
                else:
                    pass

    def main_func(self):
        # conflict_terminator = Terminator()
        result_list = self.start()
        compute = self.computation(result_list)
        if compute == 0:
            time.sleep(2)
            print("再来一次。。。")
            return self.main_func()
        else:
            time.sleep(1)
            print("计算完成，终端关闭！")


if __name__ == '__main__':
    x = Terminator()
    x.main_func()

    # test
    # test_list= [['哥哥', '剪刀'], ['艳艳', '布']]
    # y = Terminator()
    # y.computation(test_list)




