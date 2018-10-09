
def pp(f):
    '''Create latex fraction if needed'''
    if f.denominator != 1:
        if f.numerator < 0:
            return '-\\frac{{{}}}{{{}}}'.format(abs(f.numerator), f.denominator)
        else:
            return '\\frac{{{}}}{{{}}}'.format(f.numerator, f.denominator)
    else:
        return str(f.numerator)

def tformat(a, basis, pivot=None, name='x'):
    out = []
    row = ['   ']
    for c in range(len(a[0])-1):
        row.append('{}_{}'.format(name, c+1))
    row.append('RHS \\\\\n\\hline\n')

    out.append(' & '.join(row))
    basis = [''] + basis
    for i, (r, label) in enumerate(zip(a, basis)):
        label = 'z' if not label else '{}_{}'.format(name, label)
        row = [label]
        for j, value in enumerate(r):
            if (i, j+1) == pivot:
                row.append('\\boxed{{{}}}'.format(pp(value)))
            else:
                row.append('{}'.format(pp(value)))
        out.append(' & '.join(row) + ' \\\\[2pt]\n')
        if label == 'z':
            out.append('\\hline\n')

    template = '''\
$$
\\begin{{array}}{{r|{}|r}}
{}\\end{{array}}
$$
'''
    array = ''.join(out)
    return template.format('r'*(len(a[0])-1), array)
    

if __name__ == '__main__':
    import numpy as np
    lp = np.array([\
        [0, 0, 0, 0, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 0, 0, 10],
        [1, -1, 2, -1, 0, 1, 0, 12],
        [-1, 1, 1, 1, 0, 0, 1, -6]])
    print(tableau(lp, [5,6,7]))

