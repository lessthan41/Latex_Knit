
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

if __name__ == '__main__':
    cols = 1
    elements = [2, 'x+y', 3, 8.5, 4, 888]

    mat = matrix(cols, elements)
    print(mat)
