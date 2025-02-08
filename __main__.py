from my_estructure import UniqueNumbers

def main():
    input_file = "input.txt"
    output_file = "output.txt"
    unique_numbers = UniqueNumbers()

    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            number = int(line.strip())
            if unique_numbers.add_number(number):
                outfile.write(f"{number} inédito\n")
            else:
                outfile.write(f"{number} repetido\n")

    print("Números armazenados:", ", ".join(map(str, unique_numbers.numbers)))

if __name__ == "__main__":
    main()