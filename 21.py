import os
import re



def read_file_as_list(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

class Monke:
    def __init__(self,
                 ptr_1,
                 ptr_2,
                 op,
                 name=None,
                 value=None):

        self.name = name
        self.value = value
        self.ptr_1 = ptr_1
        self.ptr_2 = ptr_2
        self.op = op

    def __repr__(self):
        if self.value is None:
            return f'{self.name.upper()}: {self.ptr_1} {self.op} {self.ptr_2}'
        else:
            return f'{self.name.upper()}, {self.value}'

class All_monke:
    def __init__(self, input_monkes):
        self.all = input_monkes

    def find_monke(self, find_name):
        i = 0
        res = None
        while res is None:
            if self.all[i].name == find_name:
                res = self.all[i]
            else:
                i=i+1

        return res


def parse_puzz_input(puzz_input_raw):
    all_monke = []

    for l in puzz_input_raw:

        name = re.findall(pattern=r'^\w{4}(?=:)', string=l)[0]
        v = re.findall(pattern= r'\d+', string = l)
        if len(v)==0:
            v = None
            ptr_1 = re.findall(pattern= r'\w{4}(?= \S \w{4}$)', string = l).pop()
            ptr_2 = re.findall(pattern=r'(?<=\w{4} \S )\w{4}$', string=l).pop()
            op = re.findall(pattern=r'(?<=\w{4} )\S(?= \w{4}$)', string=l).pop()
        else:
            v = v[0]
            ptr_1 = None
            ptr_2 = None
            op = None

        new_monke = Monke(name = name, value = v, ptr_1 = ptr_1, ptr_2 = ptr_2, op = op)
        all_monke.append(new_monke)


    return all_monke


puzz_input_raw = read_file_as_list('21_ex.txt')
all_monke = All_monke(parse_puzz_input(puzz_input_raw))

all_monke.find_monke('pppw')

