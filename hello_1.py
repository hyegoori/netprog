# 1번
# friends = ["아현", "선주", "민지"]

# friends.insert(0, "예인")
# friends.insert(2, "은혜")
# friends.append("은지")

# # 결과 출력
# print(friends)

#2번
# numbers = [1, 2, 3]

# numbers[1] = 17

# numbers.extend([4, 5, 6])
# numbers.pop(0)
# numbers.sort()
# numbers.sort(reverse=True)
# numbers.insert(3, 25)

# print(numbers)

#3번
# from random import randint

# money = 50

# while money > 0 and money < 100:
#     print(f"현재 가진 돈: ${money}")
#     guess = input("동전의 앞면(1) 또는 뒷면(2)을 선택하세요: ")

#     if guess not in ['1', '2']:
#         print("잘못된 입력입니다. 1 또는 2만 입력하세요.")
#         continue
    
#     coin = randint(1, 2)
  
#     if str(coin) == guess:
#         print("맞췄습니다!")
#         money += 9
#     else:
#         print("틀렸습니다.")
#         money -= 10

# if money <= 0:
#     print("모든 돈을 잃었습니다. 게임이 종료됩니다.")

# elif money >= 100:
#     print("축하합니다! $100을 달성했습니다. 게임에서 승리하셨습니다.")

# 4번
# def gcd(a, b):
#     lager = 0
#     smaller = 0
#     if (a > b):
#         lager = a
#         smaller = b
#     else:
#         lager = b
#         smaller = a
        
#     while smaller > 0:
#         rem = lager % smaller
#         lager = smaller
#         smaller = rem
#     return lager

# if __name__ == "__main__":
#     res = gcd(16,24)
#     print(res)


#5번
# word = input("Your word: ")

# a_index = word.find('a')

# if a_index != -1:  # 'a'가 단어 안에 존재하는 경우
#     print(word[:a_index+1])  # 'a'까지의 문자열 출력
#     print(word[a_index+1:])  # 나머지 문자열 출력
# else:
#     print("'a'가 없습니다.")

#6번

# #0~49
# list_0_to_49 = [i for i in range(50)]
# print(list_0_to_49)

# #0~49 제곱
# list_squares = [i**2 for i in range(50)]
# print(list_squares)


#7번
# days = {'January':31, 'February':28, 'March':31, 'April':30, 
# 'May':31, 'June':30, 'July':31, 'August':31,
# 'September':30, 'October':31, 'November':30, 
# 'December':31}

# user_input = input("월을 입력하세요 (예: January 또는 Jan): ")
# if len(user_input) == 3:
#     for month in days:
#         if month.startswith(user_input.capitalize()):
#             print(f"{month}: {days[month]}일")
# else:
#     print(f"{user_input}: {days.get(user_input, '잘못된 입력입니다.')}일")


# print("\n알파벳 순서로 모든 월:")
# for month in sorted(days.keys()):
#     print(month)


# print("\n일수가 31인 모든 월:")
# for month, day in days.items():
#     if day == 31:
#         print(month)


# print("\n월의 일수를 기준으로 오름차순으로 (월-일수):")
# for month in sorted(days, key=days.get):
#     print(f"{month}: {days[month]}일")


# # 8번
# d = [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
# {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
# {'name':'Princess', 'phone':'555-3141', 'email':''},
# {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

# print("전화번호가 8로 끝나는 사용자:")
# for person in d:
#     if person['phone'].endswith('8'):
#         print(person['name'])

# print("\n이메일이 없는 사용자:")
# for person in d:
#     if not person['email']:
#         print(person['name'])

# user_name = input("\n사용자 이름을 입력하세요: ")
# user_found = False
# for person in d:
#     if person['name'] == user_name:
#         user_found = True
#         print(f"이름: {person['name']}, 전화번호: {person['phone']}, 이메일: {person['email']}")
#         break

# if not user_found:
#     print("이름이 없습니다.")


# 9번
# def parse_string_to_dict(input_string, delimiter1='&', delimiter2='='):
#     result_dict = {}
    
#     pairs = input_string.split(delimiter1)
    
#     for pair in pairs:
#         key, value = pair.split(delimiter2)
#         result_dict[key] = value
    
#     return result_dict

# input_string = 'led=on&motor=off&switch=off'
# result = parse_string_to_dict(input_string)

# print(result)

# 10번
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def getName(self):
#         print(self.name)

#     def getAge(self):
#         print(self.age)

# class Employee(Person):
#     def __init__(self, name, age, employeeID):
#         super().__init__(name, age)
#         self.employeeID = employeeID

#     def getID(self):
#         print(self.employeeID)

# employee = Employee("IoT", 65, 2018)

# employee.getName()  
# employee.getAge()   
# employee.getID()    



