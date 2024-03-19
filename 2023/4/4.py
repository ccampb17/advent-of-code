import os
import re

os.chdir('2023/4')


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
    # tidy up and split into lines
    lines = [re.sub(pattern=r'Card \d+: ', repl='', string=x) for x in puzz_input_raw]
    lines = [re.sub(pattern=r'\s+', repl=' ', string=x) for x in lines]
    lines = [l.split(' | ') for l in lines]

    lines_parsed = []
    for l in lines:
        cards = [x.split(' ') for x in l]
        cards = [set(x) for x in cards] # necessary?
        lines_parsed.append(cards)

    return lines_parsed

def calc_card_value(card):
    score = len(card[0].intersection(card[1]))-1

    if score >=0:
        return 2**(score)
    else:
        return 0


def puzz_solve(puzz_input_parsed):
    total = [calc_card_value(x) for x in puzz_input_parsed]
    return sum(total)



puzz_input_raw = read_file_as_list('inp_1.txt')
puzz_input_parsed = parse_puzz_input(puzz_input_raw)
puzz_solution = puzz_solve(puzz_input_parsed)


# part_2





