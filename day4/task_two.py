def main():
    
    with open("data.txt", "r") as file:
        count = 0
        for line in file:
            assignment_one, assignment_two = line.split(',')
            
            first_number_assignment_one, second_number_assignment_one = assignment_one.split('-')
            first_number_assignment_two, second_number_assignment_two = assignment_two.split('-')
            
            if int(first_number_assignment_two) >= int(second_number_assignment_two) and int(first_number_assignment_one) <= int(second_number_assignment_two):
                count += 1
            elif int(second_number_assignment_two) >= int(first_number_assignment_two) and int(first_number_assignment_two) <= int(second_number_assignment_one):
                count += 1
                
        print(count)
            

if __name__ == "__main__":
    main()
