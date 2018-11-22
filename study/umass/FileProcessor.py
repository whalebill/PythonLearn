from study.umass import FileScanner

FILE_PATH = '/study/resources/test.txt'


def getOldest(names, ages):
    max_age = max(ages)
    index_max_ages = [index for index, value in enumerate(ages) if value == max_age]
    oldest = []
    for index in index_max_ages:
        oldest.append(names[index])
    return oldest


def getTotalNum(names):
    return len(names)


def getOldestDOB(names, dobs):
    dob_num = []
    for dob in dobs:
        dob_num.append(dob.replace('-', ''))
    min_dob = min(dob_num)
    index_min_dobs = [index for index, value in enumerate(dob_num) if value == min_dob]
    oldest_dobs = []
    for index in index_min_dobs:
        oldest_dobs.append(names[index])
    return oldest_dobs


names = []
ages = []
dobs = []

f = FileScanner.read_file(FILE_PATH)
# FileScanner.print_file(FILE_PATH)

for index, line in enumerate(f):
    if line.strip() != '':
        words = line.strip().split(',')
        names.append(words[0])
        ages.append(words[1])
        dobs.append(words[2])

num_of_people = getTotalNum(names)
print('Total: ' + num_of_people.__str__())
oldest = getOldest(names, ages)
print('People with greatest age: ' + oldest.__str__())
oldest_dob = getOldestDOB(names, dobs)
print('People with greatest date of birth: ' + oldest_dob.__str__())

