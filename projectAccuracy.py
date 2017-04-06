import glob


def project_Accuracy():
    file_count = 0
    sum_of_all = 0
    for filename in glob.iglob('./data/**/accuracy.txt', recursive=True):
        file_count += 1
        with open(filename,"r") as f:
            value = float(f.readline()[:-1])
            sum_of_all += value

    print(sum_of_all/file_count)

project_Accuracy()