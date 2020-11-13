
def main(title, author, date, subproblem_cnt):
    main_content = ''
    problem_content = ''
    for p in range(len(subproblem_cnt)):
        problem_content += '\section*{Problem %d}\n' % (p + 1)
        if subproblem_cnt[p] != 1:
            for i in range(subproblem_cnt[p]):
                problem_content += '\subsection*{(%s)}\n' % chr(97 + i)
        problem_content += '\n'
    with open('sample/homework.tex', 'r') as fr:
        main_content = fr.read() % (title, author, date, problem_content)
    return main_content



title = 'Machine Learning Homework 3'
author = 'B06208030 Cheng-Yu Ho \\\\ Department of Geography'
date = 'November 2020'
subproblem_cnt = [1] * 20 # 每個 Problem 有幾個 sub-Problem

if __name__ == '__main__':
    content = main(title, author, date, subproblem_cnt)
    print(content)
