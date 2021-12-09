def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    file = []
    with open(csv_file_path, 'r') as a:
        f = a.readlines()
        for line in f:
            data = line.split(",")
            data_row = []
            for i in data:
                if i.isdigit():
                    data_row.append(float(i))
                else:
                    data_row.append(i)
        file.append(data_row)
    return file

