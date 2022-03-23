#average_from_inputfile

numbersfile = open('numbers.txt', 'r')

number_sum = 0
counter = 0

for line in numbersfile:
    counter = counter +1
    number_sum += float(line)

    print(f'I read in {counter} number(s) Current number is {float(line)} is {number_sum}')

print('Average: ', number_sum / counter)
