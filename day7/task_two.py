
import sys

def main():

    use_sample_data = sys.argv[1] if len(sys.argv) > 1 else None
    data_file = "data.txt" if not use_sample_data else "sample-data.txt"

    with open(data_file, "r") as file:
        for line in file:
            print('do something')

if __name__ == "__main__":
    main()
