
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result


csv_gen = csv_reader("generator_csv.txt")
row_count = 0

for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")