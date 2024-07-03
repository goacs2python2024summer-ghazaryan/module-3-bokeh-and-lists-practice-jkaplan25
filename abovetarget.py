def main():
    # Take input to be passed into above target function.
    '''
    Input is as follows:
    List of data, passed into nums, that the user provides separated by spaces, i.e '1 2 42 4 1 2.4'
    The number passed into target nums
    and whether or not the user would like a boolean returned or the list of which numbers in the list are bigger than target_num.
    '''
    print(above_target([float(num) for num in input('Please enter the set of data that you would like to compare against your number:').split(' ')], float(input('Please enter your number:')), input('Y/N: Would you like detailed results?').lower().startswith('y')))
def above_target(nums, target_num, detailed=False):
    bigger_nums = [x for x in nums if x > target_num]
    if detailed:
        return bigger_nums
    else:
        return bool(bigger_nums)
if __name__ == '__main__':
    main()
