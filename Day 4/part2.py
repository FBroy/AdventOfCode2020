import re


with open("input.txt") as f:
    lines = f.read().split("\n\n")
    keywords = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    valid = 0
    for passport in lines:
        tmp = passport
        passport = passport.replace("\n", " ").split(" ")
        boolean = True
        for line in passport:
            for keyword in keywords:
                if not(keyword in tmp):
                    boolean = False
                    break
                if keyword in line:
                    line = line.split(":")
                    if keyword == "byr:":
                        if not(1920 <= int(line[1]) <= 2002):
                            boolean = False
                            break
                    elif keyword == "iyr:":
                        if not(2010 <= int(line[1]) <= 2020):
                            boolean = False
                            break
                    elif keyword == "eyr:":
                        if not(2020 <= int(line[1]) <= 2030):
                            boolean = False
                            break
                    elif keyword == "hgt:":
                        if "cm" in line[1]:
                            if not(line[1][0].isnumeric() and line[1][1].isnumeric() and line[1][2].isnumeric()):
                                boolean = False
                                break
                            elif not(150 <= int(line[1][0]+line[1][1]+line[1][2]) <= 193):
                                boolean = False
                                break
                        elif "in" in line[1]:
                            if not(line[1][0].isnumeric() and line[1][1].isnumeric()):
                                boolean = False
                                break
                            elif not (59 <= int(line[1][0]+line[1][1]) <= 76):
                                boolean = False
                                break
                        else:
                            boolean = False
                            break
                    elif keyword == "hcl:":
                        if len(line[1]) != 7:
                            boolean = False
                            break
                        elif not(re.search("^#[0-9a-f]{6}", line[1])):
                            boolean = False
                            break
                    elif keyword == "ecl:":
                        if not(line[1] == "amb" or line[1] == "blu" or line[1] == "brn" or line[1] == "gry"\
                            or line[1] == "grn" or line[1] == "hzl" or line[1] == "oth"):
                            boolean = False
                            break
                    elif keyword == "pid:":
                        if not(line[1].isnumeric() and len(line[1]) == 9):
                            boolean = False
                            break
                
        if boolean:
            valid += 1

print(valid)