"""
传入 任意 column name 获取所有行

created_time = 20190325

created_by = tzh
"""
import pandas as pd


class ReadExcel(object):
    def __init__(self, excel_name):
        self.excel_name = excel_name

    def get_content(self, *args):
        """获取列内容"""
        df = pd.read_excel(self.excel_name)
        num = len(df)
        x = []
        for i in range(num):
            each_line = []
            for each in args:
                one_target = df.at[i, each]
                each_line.append(one_target)
            x.append(each_line)
        return x


class Execute(object):
    pass


if __name__ == '__main__':
    name = 'target.xlsx'
    x = ReadExcel(name)
    print(x.get_content('TABLE_COMMENT', 'TABLE_TYPE'))
