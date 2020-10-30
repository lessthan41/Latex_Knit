
def table(caption, row_name, col_name, elements):
    thead = row_name + ' & '
    tbody, content  = '', ''
    cols = len(col_name)

    for i in range(cols): # thead
        thead += '\\textbf{%s}' % col_name[i]
        if i == cols - 1:
            thead += ' \\\\'
        else:
            thead += ' & '

    # row_cnt = 1
    # for i in range(len(elements)): # tbody
    #     if (i + 1) % cols == 0:
    #         tbody += ' \\\\ \n'
    #         tbody += str(row_cnt)
    #         row_cnt += 1
    #     else:
    #         if i != 0: tbody += ' & '
    #         tbody += str(elements[i])

    with open('sample/table.tex', 'r') as fr:
        content = fr.read() % (caption, 'c' * len(col_name), thead, tbody)
    return content


if __name__ == '__main__':

    caption = 'test table'
    col_name = ['col1', 'col2', 'col3']
    row_name = 'rowname'
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    tab = table(caption, row_name, col_name, elements)

    print(tab)
