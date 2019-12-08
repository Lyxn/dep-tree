def read_sexp(filename):
    terms = []
    with open(filename) as f:
        for line in f:
            if line.startswith("#"):
                continue
            i = 0
            s = 0
            ret = line.strip()
            while i < len(ret):
                char = ret[i]
                if char == '(':
                    terms.append(char)
                    s = i + 1
                elif char == ')':
                    if 0 < s < i:
                        terms.append(ret[s:i])
                        s = 0
                    terms.append(char)
                i += 1
            if 0 < s < i:
                terms.append(ret[s:i])
    return terms


def test():
    filename = "./data/dep0.txt"  # gbk
    # filename = "./data/dep0.s"
    terms = read_sexp(filename)
    print(terms)


if __name__ == '__main__':
    test()
