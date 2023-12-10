import math


class Solution:
    def __init__(self):
        self.data = []

    def load_data(self, file_name: str):
        with open(file_name) as f:
            self.data = f.read().splitlines()

    def solve_part1(self):
        sum = 0
        for line in self.data:
            first_digit = 0
            last_digit = 0
            for letter in line:
                if letter.isdigit():
                    first_digit = int(letter)
                    break

            for letter in line[::-1]:
                if letter.isdigit():
                    last_digit = int(letter)
                    break

            sum += first_digit * 10 + last_digit

        print("Part 1 Answer:", sum)

    def solve_part2(self):
        dict = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }

        sum = 0
        for line in self.data:
            first_digit_index = math.inf
            last_digit_index = 0
            first_digit = 0
            last_digit = 0
            for key in dict:
                if key in line:
                    if line.index(key) < first_digit_index:
                        first_digit_index = line.index(key)
                        first_digit = dict[key]

                    reversed_line = line[::-1]

                    if key[::-1] in reversed_line:
                        if len(line) - reversed_line.index(key[::-1]) - 1 > last_digit_index:
                            last_digit_index = len(line) - reversed_line.index(key[::-1]) - 1
                            last_digit = dict[key]

            for letter in line:
                if line.index(letter) < first_digit_index:
                    if letter.isdigit():
                        first_digit = int(letter)
                        break

            for i, letter in enumerate(line[::-1]):
                if len(line) - i > last_digit_index:
                    if letter.isdigit():
                        last_digit = int(letter)
                        break

            sum += first_digit * 10 + last_digit

        print("Part 2 Answer:", sum)
