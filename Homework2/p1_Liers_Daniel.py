"""
@author: Daniel Liers
ZNumber: 23716566
"""
def line_number(input_file: str, output_file: str) -> None:
    """Reads a file"""
    try:
        infile = open(input_file, "r")
        outfile = open(output_file, "w")

        number = 1

        for line in infile:
            outfile.write(f"{number}. {line}")
            number = number + 1
        infile.close()
        outfile.close()

    except Exception as e:
        print("Error:", e)
        raise

def parse_functions(filename: str) -> tuple:
    
    try:
        infile = open(filename, "r")
        lines = infile.readlines()
        infile.close()
        functions = []

        for i in range(len(lines)):
            if lines[i].startswith("def "):
                line = lines[i]

                name = line.split("def ")[1].split("(")[0]
                arguments = line.split("(")[1].split(")")[0]
                code = []
                code.append(line.split("#")[0].rstrip())
                j = i + 1

                while j < len(lines):
                    if lines[j].strip() == "":
                        j = j + 1
                    elif lines[j].strip().startswith("#"):
                        j = j + 1
                    elif lines[j][0] == " " or lines[j][0] == "\t":
                        code.append(lines[j].split("#")[0].rstrip())
                        j = j + 1
                    else:
                        break

                function_code = "\n".join(code) + "\n"
                functions.append(
                    (i + 1, name, arguments, function_code)
                )

        functions.sort()

        return tuple(functions)

    except Exception as e:
        print("Error:", e)
        raise

def main() -> None:
    line_number("test.py", "test.py.txt")
    result = parse_functions("funs.py")
    print(result)

if __name__ == "__main__":
    main()