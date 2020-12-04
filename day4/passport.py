import re

class Field:
    def __init__(self, regex, min_value, max_value):
        self.regex = regex
        self.min_value = min_value
        self.max_value = max_value

    def check_in_range(self, input_value):
        if self.min_value is not None and self.max_value is not None:
            return self.min_value <= int(input_value) <= self.max_value
        else:
            return True

    def check_if_valid(self, input_value):
        if not re.search(self.regex, input_value):
            return False

        return self.check_in_range(input_value)


class HeightField(Field):
    def check_in_range(self, input_value):
        unit = input_value[-2:]
        return self.min_value[unit] <= int(input_value[:-2]) <= self.max_value[unit]
        


fields = {"byr": Field("^\d{4}$", 1920, 2002), 
          "iyr": Field("^\d{4}$", 2010, 2020), 
          "eyr": Field("^\d{4}$", 2020, 2030),
          "hgt": HeightField("^\d+(cm|in)$", {"cm": 150, "in": 59}, {"cm": 193, "in": 76}),
          "hcl": Field("^#[0-9a-f]{6}$", None, None),
          "ecl": Field("^amb|blu|brn|gry|grn|hzl|oth$", None, None),
          "pid": Field("^\d{9}$", None, None)}


passports = [] 
with open("passports.txt", "r") as file:
    passports = list(map(lambda passp: passp.replace("\n", " "), file.read().split("\n\n")))


def count_valid_passports():
    valid_passports = 0
    for passport in passports:
        valid = True
        curr_fields = dict(field.split(":") for field in passport.split(" "))
        for must_field in fields.keys():
            if must_field not in curr_fields.keys() or not fields[must_field].check_if_valid(curr_fields[must_field]):
                valid = False
                break
        valid_passports += 1*valid

    print(valid_passports)


count_valid_passports()
