# Converts positive or negative decimal  numbers to binary

def negative_bin(binary_number):
    """Takes a binary number as string and return it's twos complement"""
    while len(binary_number) < 16:
        binary_number = '0' + binary_number

    # Ones complement
    ones_complement = ''
    for digit in binary_number:
        if digit == '1':
            digit = '0'
            ones_complement = ones_complement + digit
        else:
            digit = '1'
            ones_complement = ones_complement + digit
    
    # For easier handiling we flip the ones complement string
    flipped_ones_comp = ones_complement[::-1]
    carry = '1' # Used for the addition
    twos_complement = ''
    for char in flipped_ones_comp:
        if char == '1' and carry == '1':
            new_digit = '0'
            carry = '1'
        elif char == '0' and carry == '1':
            new_digit = '1'
            carry = '0'
        elif char == '0' and carry == '0':
            new_digit = '0'
            carry = '0'
        elif char == '1' and carry == '0':
            new_digit = '1'
            carry = '0'

        twos_complement = twos_complement + new_digit
        
    return twos_complement[::-1] # Flip again for right order


def dec_to_bin(decimal_number):
    """Takes a decimal number as integer (+ / -) and returns a binary representation as a string"""
    binary_number = ''

    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = binary_number + str(remainder)
        decimal_number = decimal_number // 2 # Condition for while loop

    return binary_number[::-1]


def main():
    valid_input = False
    while not valid_input:
        dec_number = input('Please, enter a decimal number: ')
        try:
            dec_number = int(dec_number)
            if dec_number < -32768 or dec_number > 32767:
                print('I can only handle 16-bit signed long numbers. Try again.')
            else:
                valid_input = True
        except:
            print('This is not a valid decimal number. Try again.')
    
    if dec_number > 0:
        bin_num = dec_to_bin(dec_number)
    elif dec_number < 0:
        bin_num = dec_to_bin(dec_number * -1)
        bin_num = negative_bin(bin_num)
    else:
        bin_num = dec_number

    print(f'The binary equivalent of {dec_number} is {bin_num}', len(bin_num))


if __name__ == '__main__':
    final_try = False
    while not final_try:
        main()
        answer = input('Do you want to enter another number (y/n)? ')
        if answer == 'n':
            final_try = True
        else:
            pass
