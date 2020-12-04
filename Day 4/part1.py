with open("input.txt") as f:
    lines = f.read().split("\n\n")
    keywords = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    valid = 0
    for passport in lines:
        passport = passport.replace("\n", " ")
        boolean = True
        for keyword in keywords:
            if not(keyword in passport):
                boolean = False
                break
        if boolean:
            valid += 1

print(valid)