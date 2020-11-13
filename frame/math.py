import re

def matrix(cols, elements):
    content = '$\\begin{bmatrix}'
    for eid in range(len(elements)):
        if eid == 0:
            content += ' '
        elif eid % cols == 0:
            content += ' \\\\ '
        else:
            content += ' & '
        content += str(elements[eid])
    content += ' \end{bmatrix}$'
    return content

def math_format(string):
    i = 0
    bracket = False
    strlen = len(string)
    while i < strlen:
        char = string[i]
        if char in ['_', '^']: # add bracket
            string = string[:i+1] + '{' + string[i+1:]
            bracket = True
            i += 1
        elif char == ' ' and bracket == True:
            string = string[:i] + '}' + string[i+1:]
            bracket = False
            i += 1
        elif char == '/':
            string = denominator(string, i)
            bracket = False
            i += 8
        strlen = len(string)
        i += 1
    if bracket == True: string += '}'
    return string

def denominator(string, i):
    string = string[:i] + '}{' + string[i+1:]
    idx = i
    while string[idx] != ' ':
        idx += 1
    string = string[:idx] + '}' + string[idx+1:]
    idx = i
    while string[idx] != ' ':
        idx -= 1
    string = string[:idx] + '\\frac{' + string[idx+1:]
    return string

def replacer(string, pair_list):
    new_string = string
    for round in range(len(pair_list)):
        feature, replacement = pair_list[round][0], pair_list[round][1]
        replace_indexes = [m.start() for m in re.finditer(feature, new_string)]
        for i in range(len(replace_indexes)):
            replace_indexes[i] += (len(replacement) - len(feature)) * i
        for i in replace_indexes:
            new_string = new_string[:i] + replacement + new_string[i+len(feature):]
    return new_string

if __name__ == '__main__':

    # # matrix
    # cols = 1
    # elements = [2, 'x+y', 3, 8.5, 4, 888]
    # mat = matrix(cols, elements)
    # print(mat)

    # math sentence
    # str = ' \\partial(yx^Tw)/\\partialw '
    # formatted_str = math_format(str)
    # print(formatted_str)

    # replacement
    string = """&E(u+v) \\\\
        \\approx \\quad &E(u) + b_E(u)^T ((u+v)-u) + \\frac{1}{2} ((u+v)-u)^T A_E(u) ((u+v)-u) \\\\
        = \\quad &E(u) + b_E(u)^Tv + \\frac{1}{2} v^T A_E(u) v \\\\ \\\\
        \\text{Let} \\quad &T_2(u+v) = E(u) + b_E(u)^Tv + \\frac{1}{2} v^T A_E(u) v  \\\\
        \\Rightarrow \\quad &\\frac{\\partial \\; T_2(u+v)}{\\partial \\; v} = 0\\\\
        \\Rightarrow \\quad &0 + b_E(u) + \\frac{1}{2} (A_E(u)^T + A_E(u)) v = 0 \\qquad (\\text{where $A_E(u)$ is symmetric}) \\\\
        \\Rightarrow \\quad &v = -(A_E(u))^{-1} b_E(u) \\\\ \\\\"""
    # new_string = replace(string, [('b_E', '\\text{b}_E'), ('A_E', '\\text{A}_E'), ('u', '\\textbf{u}'), ('v', '\\textbf{v}')])
    new_string = replacer(string, [('b_E', '\\text{b}_E'), ('A_E', '\\text{A}_E')])
    print(new_string)
