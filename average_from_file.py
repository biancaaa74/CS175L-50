#average_from_inputfile

import sys
def main():
    try:
        numbersfile = open('numbers.txt', 'r')
    except IOError:
        print('Error file cant be read')
        sys.exit()
    number_sum = 0
    counter = 0
    
    for line in numbersfile:
        counter = counter +1
        try:
            number_sum += float(line)
    

            print(f'I read in {counter} number(s) Current number is {float(line)} is {number_sum}')
        except ValueError:
            print('Error, bad value: skipping')
            counter = counter -1
            continue
        print('Average: ', number_sum / counter)

main()
