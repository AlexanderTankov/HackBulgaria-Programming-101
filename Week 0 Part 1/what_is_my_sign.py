def what_is_my_sign(day, month):
    if month == 1:
        if day >= 21:
            return "Aquarius"
        else:
            return "Capricorn"
    elif month == 2:
        if day >= 20:
            return "Pisces"
        else:
            return "Aquarius"
    elif month == 3:
        if day >= 21:
            return "Aries"
        else:
            return "Pisces"
    elif month == 4:
        if day >= 21:
            return "Taurus"
        else:
            return "Aries"
    elif month == 5:
        if day >= 22:
            return "Gemini"
        else:
            return "Taurus"
    elif month == 6:
        if day >= 22:
            return "Cancer"
        else:
            return "Gemini"
    elif month == 7:
        if day >= 23:
            return "Leo"
        else:
            return "Cancer"
    elif month == 8:
        if day >= 23:
            return "Virgo"
        else:
            return "Leo"
    elif month == 9:
        if day >= 24:
            return "Libra"
        else:
            return "Virgo"
    elif month == 10:
        if day >= 24:
            return "Scorpio"
        else:
            return "Libra"
    elif month == 11:
        if day >= 23:
            return "Sagittarius"
        else:
            return "Scorpio"
    elif month == 12:
        if day >= 22:
            return "Capricorn"
        else:
            return "Sagittarius"

print(what_is_my_sign(5, 8))
print(what_is_my_sign(29, 1))
print(what_is_my_sign(30, 6))
print(what_is_my_sign(31, 5))
print(what_is_my_sign(2, 2))
print(what_is_my_sign(8, 5))
print(what_is_my_sign(9, 1))
