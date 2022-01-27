# liste - exercice 2


def remove_from_list(lst):
    _lst = []
    for i in lst:
        if i != "Hello":
            _lst.append(i)
    return _lst

print(remove_from_list(["Hello","Hello","etc"]))

