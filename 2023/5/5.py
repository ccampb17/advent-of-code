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
            as_list_of_ints = [int(y) for y in x.split(' ')]
            _type_correspondences.append(as_list_of_ints)
        else:
            print(f'finished type {_corr_type}')
            correspondence_dict[_corr_type] = _type_correspondences
            type_correspondences = []


    return correspondence_dict, seed_info


puzz_input_raw = read_file_as_list('ex_1.txt')

correspondence_dict, seed_info = parse_puzz_input(puzz_input_raw)


random_key = random.choice(list(correspondence_dict.keys()))
correspondence_type = random_key

# dbg
type_from = 'seed'
type_to = 'soil'
value = seed_info[0]

# this relies heavily on indices and that's BAD CODE.

def check_correspondence_indices(value, type_from, type_to, correspondence_dict):

    # get the right correspondence
    regex = re.compile(f'^{type_from}-to-{type_to}')

    for key in correspondence_dict.keys():
        if regex.match(key):
            print(key)
            correspondence_type = correspondence_dict[key]

    # unusual_index = True
    for idx in correspondence_type:
        # for readability
        type_from_value_start = correspondence_type[0]
        type_from_value_end = correspondence_type[0] + correspondence_type[2]

        if value >= type_from_value_start and value <= type_from_value_end:

            type_from_type_to_difference = correspondence_type[1] - correspondence_type[0]

            print('found')
            corresponding_value = correspondence_type[1] + type_from_type_to_difference
            return corresponding_value

    print('no conversion required')
    return value








