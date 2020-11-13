import re

# "Машерова просп.","Центральный","1-31, 56-60"
# "Машерова просп.","Советский","2-54"
# "Танковая ул.","Центральный","67, 77, 79, 87"
hello = "1-31, 56-60а"


def make_range(text):
    nums = []
    text = re.sub(r"\s+", "", text)
    text = re.sub(r"[а-яa-z]", "", text)
    for i in text.split(','):
        me  = i.split('-')
        if len(me) > 1:
            nums.extend(list(range(int(me[0]), int(me[1]), 2)))
            nums.append(int(me[1]))
        else:
            nums.append(i)
    return nums



def is_in_range(text, building):
    nns = make_range(text)
    # print(nns)
    return True if building in nns else False

print(is_in_range(hello, 17))