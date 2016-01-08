import re


def calc_paper_required(l, w, h):
    return 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)

with open('data.txt', 'r') as f:
    content = f.readlines()
    solution = 0
    line_cnt = 0
    regex = re.compile('(\d+)x(\d+)x(\d+)')
    for line in content:
        matched = regex.match(line)
        step_result = calc_paper_required(int(matched.group(1)),
                                          int(matched.group(2)),
                                          int(matched.group(3)))
        solution += step_result
        line_cnt += 1
    print solution, line_cnt
