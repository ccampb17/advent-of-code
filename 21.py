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

    def solve(self):
        i = 0
        while self.find_monke('root').value is None:
            this_monke = self.all[i]

            print(f'Checking {this_monke.name}...')

            if this_monke.value is None:
                mon_1 = self.find_monke(this_monke.ptr_1)
                mon_2 = self.find_monke(this_monke.ptr_2)
                if mon_1.value is not None and mon_2.value is not None:
                    expr = f'{mon_1.value}{this_monke.op}{mon_2.value}'
                    this_monke.value = eval(expr)
                    print(f'found value!')

            i = i + 1
            if i >= len(self.all):
                i = 0
                print('GOING THROUGH AGAIN')

        print('the answer is: ')
        print(self.find_monke('root').value)


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



puzz_input_raw = read_file_as_list('21_input.txt')
all_monke = All_monke(parse_puzz_input(puzz_input_raw))
all_monke.solve()

