def string_expansion(txt):
    m,n = '',1
    for j in txt:
        if j.isdigit():
            n = int(j)
        else:
            m += j*n
    return m