def most_common_chars():
    a = "hello world"
    b = "abwdiwdkwdw"
    c = "aaaaa bbb cccc"
    most_common_letter = max(set(a), key = a.count)
    most_common_letter_1 = max(set(b), key = b.count)
    most_common_letter_2 = max(set(c), key = c.count)
    print(most_common_letter)
    print(most_common_letter_1)
    print(most_common_letter_2)

most_common_chars()