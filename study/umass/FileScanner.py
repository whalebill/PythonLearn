PATH = 'C:\\Users\\Junyao Luo\\PycharmProjects\\LearnPython'


def print_file(file_path):
    with open(PATH + file_path, 'r') as f:
        read_data = f.read()
    f.close()
    print(read_data)


def read_file(file_path):
    with open(PATH + file_path, 'r') as f:
        read_data = f.readlines()
    f.close()
    return read_data
