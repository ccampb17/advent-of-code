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


def parse_puzz_input(puzz_input_raw, verbose=True):

    # assumes it will be on line 0
    seed_info = re.findall(string=puzz_input_raw[0], pattern=r'\d+')
    seed_info = [int(x) for x in seed_info]

    puzz_input_no_seed_info = puzz_input_raw.copy()

    # this should be dynamic
    puzz_input_no_seed_info = puzz_input_no_seed_info[2:]

    # !JANK ALERT! so the loop knows which is the final entry
    puzz_input_no_seed_info.append('')

    # get the types dynamically
    correspondence_types_raw = [re.findall(string=x, pattern=r'\w+-to.+') for x in puzz_input_no_seed_info]

    # remove empty elements
    correspondence_types = [x[0] for x in correspondence_types_raw if x]

    # dictionary of type: the correspondence numbers
    correspondence_dict = dict()

    # instantiate hidden var for loop
    _type_correspondences = []

    x = puzz_input_no_seed_info[2]
    # dynamically construct corr dict
    for i, x in enumerate(puzz_input_no_seed_info):

        if x in correspondence_types:
            _corr_type = x

        if re.match(string=x, pattern='\d+'):
            as_list_of_ints = [int(y) for y in x.split(' ')]
            _type_correspondences.append(as_list_of_ints)

        elif len(x) == 0:
            if verbose:
                print(f'finished type {_corr_type}')
            correspondence_dict[_corr_type] = _type_correspondences
            _type_correspondences = []


    return correspondence_dict, seed_info



type_from = 'light'
type_to = 'temperature'
value = 74
# this relies heavily on indices and that's BAD CODE.

def do_single_type_conversion(value, type_from, type_to, correspondence_dict, verbose=True):

    if verbose:
        print(f'now converting: {value}')

    # get the right correspondence
    regex = re.compile(f'^{type_from}-to-{type_to}')

    for key in correspondence_dict.keys():
        if regex.match(key):
            if verbose:
                print(f'{key}')
            correspondence_type = correspondence_dict[key]


    for idx in correspondence_type:

        # for readability
        type_from_value_start = idx[1]
        type_from_value_end = idx[1] + (idx[2]-1)

        type_to_value_start = idx[0]
        type_to_value_end = idx[2] + (idx[2]-1)

        if value >= type_from_value_start and value <= type_from_value_end:

            # convert the from value to the to value...
            type_from_type_to_difference = idx[0] - idx[1]

            if verbose:
                print('found')
            corresponding_value = value + type_from_type_to_difference
            return corresponding_value


    # or do no conversion (1-1 conversion as per the documentation)
    if verbose:
        print('no conversion required')
    return value

def do_full_conversion(seed_value, correspondence_dict, verbose = True):

    all_types_ordered = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
    i=0

    result = seed_value
    for i, x in enumerate(all_types_ordered):
        if verbose:
            print(i)
        if i < len(all_types_ordered)-1:
            result = do_single_type_conversion(value = result,
                                               type_from=all_types_ordered[i],
                                               type_to=all_types_ordered[i+1],
                                               correspondence_dict=correspondence_dict,
                                               verbose=verbose)


    return result

def solve_puzzle_1(input_path):

    puzz_input_raw = read_file_as_list(input_path)

    correspondence_dict, seed_info = parse_puzz_input(puzz_input_raw)

    all_results = []
    for value in seed_info:
        res = do_full_conversion(value, correspondence_dict)
        all_results.append(res)

    return min(all_results)

solve_puzzle_1('inp_1.txt')
# > 226172555

##### PART 2 #####

from tqdm import tqdm

def generate_seed_range(seed_info):

    seed_range = []

    for i in tqdm(range(0, len(seed_info), 2)):
        # this_range = []

        # readability
        range_start = seed_info[i]
        range_stop = range_start + seed_info[i+1]

        for j in range(range_start, range_stop):

            # this_range.append(j) # no need to keep separate lists
            seed_range.append(j)

        # seed_range.append(this_range)

    return seed_range

input_path = 'inp_1.txt'
def solve_puzzle_2(input_path):
    puzz_input_raw = read_file_as_list(input_path)

    correspondence_dict, seed_info = parse_puzz_input(puzz_input_raw)

    seed_range = generate_seed_range(seed_info)

    all_results = []

    print(f'starting range conversion of {len(seed_range)} values...')

    for value in tqdm(seed_range):

        res = do_full_conversion(value, correspondence_dict, verbose=False)
        all_results.append(res)

    print('finished')
    return min(all_results)

solve_puzzle_2('inp_1.txt')


