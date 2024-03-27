import os
import re

import random # for testing

if not re.findall(string=os.getcwd(), pattern=r'2023[/\\\\]5'):
    os.chdir('2023/5')

def read_file_as_list(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []


def parse_puzz_input(puzz_input_raw):

    # assumes it will be on line 0
    seed_info = re.findall(string=puzz_input_raw[0], pattern=r'\d+')

    puzz_input_no_seed_info = puzz_input_raw.copy()

    # this should be dynamic
    puzz_input_no_seed_info = puzz_input_no_seed_info[2:]

    # get the types dynamically
    correspondence_types_raw = [re.findall(string=x, pattern=r'\w+-to.+') for x in puzz_input_no_seed_info]

    # remove empty elements
    correspondence_types = [x[0] for x in correspondence_types_raw if x]

    # dictionary of type: the correspondence numbers
    correspondence_dict = dict()

    # instantiate hidden var for loop
    _type_correspondences = []

    # dynamically construct corr dict
    for i, x in enumerate(puzz_input_no_seed_info):
        print(x)
        if x in correspondence_types:
            _corr_type = x

        if re.match(string=x, pattern='\d+'):
            _type_correspondences.append(x)
        else:
            print(f'finished type {_corr_type}')
            correspondence_dict[_corr_type] = _type_correspondences
            type_correspondences = []


    return correspondence_dict


puzz_input_raw = read_file_as_list('ex_1.txt')

correspondence_dict = parse_puzz_input(puzz_input_raw)


random_key = random.choice(list(correspondence_dict.keys()))
correspondence_type = random_key


def create_correspondence_indices(correspondence_type, correspondence_dict):
    sou





