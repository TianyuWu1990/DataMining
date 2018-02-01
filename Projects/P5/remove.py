import csv

def read_file(file):
    with open(file, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data
txt_file = r"winemag-data_first150k.csv"
csv_file = r"winemag-data_first150k_remove.csv"

in_txt = read_file(txt_file)
out_csv = csv.writer(open(csv_file, 'wb'))
out_txt = []
for row in in_txt:
    out_txt.append([
        "".join(a if ord(a) < 128 else '' for a in i)
        for i in row
    ])


out_csv.writerows(out_txt)