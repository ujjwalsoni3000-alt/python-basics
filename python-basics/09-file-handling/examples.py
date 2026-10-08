with open("sample.txt", "w") as f:
    f.write("Line one\n")
    f.write("Line two\n")

with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())
