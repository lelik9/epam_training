try:
    from Tools.scripts.treesync import raw_input
except ImportError:
    pass
from math import sqrt


def inp():
    nums = raw_input('Enter digits separated by ",": ').split(',')

    try:
        nums = [int(i) for i in nums]
    except ValueError:
        print('You must enter only digits separated by ","\n')
        return
    return nums

if __name__ == '__main__':
    while True:
        a = raw_input('Enter string:')

        if len(a) < 10:
            print('string too short')

        else:
            print(a[:4])
            print(a[-5:-1])
            print(a[len(a)//2])
            print(a[2:8])
            break

    while True:
        nums = inp()

        if nums:
            print('4th element: {}'.format(nums[3]))

            nums.reverse()
            avg = (sum(nums)) / len(nums)
            dev_avg = [abs(i - avg) for i in nums]
            avg_sqrt = sqrt((sum(dev_avg) / len(nums)))
            multiply_seven = [i for i in range(1, 500) if i % 7 == 0]

            print('Reversed elemtnts: {}'.format(str(nums)))
            print('Sum of all elements: {}'.format(sum(nums)))
            print('Average: {}'.format(avg))
            print('Deviation from average: {}'.format(str(dev_avg)))
            print('Sqrt: {}'.format(avg_sqrt))
            print('Multiply seven in range 1-500: {}'.format(multiply_seven))

            nums = inp()
            res = [i**2 for i in nums if i % 2 != 0]

            print('odd numbers: {}'.format(str(res)))
            break
