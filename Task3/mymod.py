def proper_file_name(name):
    if name.find('.txt') == -1:
        name += '.txt'
    return name


def count_lines(name):
    try:
        name = proper_file_name(name)
        with open(name, 'r') as file_object:
            count = 0
            for line in file_object:
                count += 1
                last_line = line
            if ord(last_line[-1]) == 10:
                count += 1
            return count
    except FileNotFoundError:
        print('There is no such file in this directory!')


def count_chars(name):
    try:
        name = proper_file_name(name)
        with open(name, 'r') as file_object:
            full_file = file_object.read()
            full_file = full_file.replace(' ', '').replace('\n', '')
            return len(full_file)
    except FileNotFoundError:
        print('There is no such file in this directory!')


def test(name):
    name = proper_file_name(name)
    print(f'File \'{name}\' has {count_lines(name)} lines in it')
    print(f'File \'{name}\' has {count_chars(name)} characters without space in it')
