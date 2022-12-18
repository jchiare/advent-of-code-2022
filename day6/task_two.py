
import sys

def main():

    use_sample_data = sys.argv[1] if len(sys.argv) > 1 else None
    data_file = "data.txt" if not use_sample_data else "sample-data.txt"

    with open(data_file, "r") as file:
        last_four_chars = []
        for line in file:
            for i in range(0,len(line)):
                
                
                last_four_chars.append(line[i])
                if len(last_four_chars) >= 15:
                    del last_four_chars[0]
                
                unique_last_four_chars = list(set(last_four_chars))
                
                if len(unique_last_four_chars) == 14:
                    print('index: ', i + 1)
                    break

if __name__ == "__main__":
    main()
