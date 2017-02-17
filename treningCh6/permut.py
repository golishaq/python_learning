def check_permutation(str1, str2):
    if len(str1) is not len(str2):
        return False

    while len(str1) > 0 and len(str2) > 0:
        char_1 = str1[0]
        char_2 = str2[len(str2) - 1]

        str1 = str1[1:]
        str2 = str2[:-1]

        if char_1 == char_2:
            continue
        else:
            return False
    return True

def main():
    a = check_permutation("cat", "tac")
    b = check_permutation("apple", "aaaae")
    c = check_permutation("a", "a")

    print(a, b, c)

main()
