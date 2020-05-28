from csvreader import CsvReader


with CsvReader('good.csv', skip_top=5, skip_bottom=1) as file:
    if not file:
        print("File is corrupted")
        exit(1)
    data = file.getdata()
    print(*data, sep="\n")
    header = file.getheader()
