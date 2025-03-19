def xyz_there(str):
    if str.startswith("xyz"):
        return True

    for i in range(1, len(str) - 2):
        if str[i - 1] != '.' and str[i] == 'x' and str[i + 1] == 'y' and str[i + 2] == 'z':
            return True

    return False
