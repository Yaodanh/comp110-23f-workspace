"""dictionary.py."""
__author__ = "703707593"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of the inp_dict."""
    invert_dic: dict[str, str] = {}
    for i in inp_dict:
        if inp_dict[i] in invert_dic:
            raise KeyError
        else:
            invert_dic[inp_dict[i]] = i
    return invert_dic


def count(list1: list[str]) -> dict[str, int]:
    """Count the frequencies of numbers."""
    new_dict: dict[str, int] = {}
    for item in list1:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict


def favorite_color(d: dict[str, str]) -> str:
    """Find the most popular color."""
    color_list: list[str] = []
    for color in d:
        color_list.append(d[color])
    color_count = count(color_list)
    max_count: int = 0
    favorite: str = ""
    for color in color_count:
        if color_count[color] > max_count:
            max_count = color_count[color]
            favorite = color
    return favorite
            

def alphabetizer(list2: list[str]) -> dict[str, list[str]]:
    """Classify by the first letter."""
    a_dict: dict[str, list[str]] = {}
    for word in list2:
        first_letter = word[0].lower()
        if first_letter in a_dict:
            a_dict[first_letter].append(word)
        else:
            a_dict[first_letter] = [word]
    return a_dict

        
def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Check the attendance."""
    if day in attendance_log:
        if student not in attendance_log[day]:
            attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]
    return attendance_log