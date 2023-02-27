from random import randint


def generate_numbers(n):
    numbers = []
    for i in range(n):
        num = randint(1,45)
        if num not in numbers:
            numbers.append(num)
    return numbers


def draw_winning_numbers():
    winning_numbers=generate_numbers(7)
    return sorted(winning_numbers[:6])+winning_numbers[6:]

#print(draw_winning_numbers())

# def count_matching_numbers(numbers, winning_numbers):
#     count=0
#     list1=[]
#     list2=[]
#     list1=numbers
#     list2=winning_numbers
#     for i in range(len(winning_numbers)):
#         for k in range(len(numbers)):
#             if numbers[k]==winning_numbers[i]:
#                 count = count+1
#     return count
# 다른 방법으로 코드 축소화 시키기
# 밑에가 축소화된 코드
def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count = count +1
    return count


def check(numbers, winning_numbers):
    if count_matching_numbers(numbers,winning_numbers[:6]) == 6:
        return 1000000000
    elif count_matching_numbers(numbers,winning_numbers[:6]) == 5 and count_matching_numbers(numbers,winning_numbers[6:]) == 1:
        return 50000000
    elif count_matching_numbers(numbers,winning_numbers[:6]) == 5:
        return 1000000
    elif count_matching_numbers(numbers,winning_numbers[:6]) == 4:
        return 50000
    elif count_matching_numbers(numbers,winning_numbers[:6]) == 3:
        return 5000
    else:
        return 0

