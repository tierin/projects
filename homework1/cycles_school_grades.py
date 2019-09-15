school_grades = [dict(school_class='4a', scores=[3, 4, 4, 5, 2, 3, 3, 4, 3, 2, 4, 5, 5, 4]),
                 {'school_class': '4b', 'scores': [3, 4, 3, 4, 4, 3, 5, 5, 5, 3, 4, 3, 4, 4, 5, 2]},
                 {'school_class': '3a', 'scores': [3, 2, 4, 4, 5, 3, 5, 2, 5, 3, 2, 5, 2, 3, 4, 3, 3, 4, 5]},
                 {'school_class': '3b', 'scores': [5, 5, 5, 5, 4, 3, 4, 5, 5, 4, 5, 4, 5, 4, 3]},
                 {'school_class': '2a', 'scores': [3, 3, 3, 3, 4, 5, 5, 3, 4, 5, 3, 4, 4, 5, 2]},
                 {'school_class': '2b', 'scores': [3, 4, 5, 3, 4, 3, 3, 5, 5, 3, 4, 5, 4, 3]},
                 {'school_class': '1a', 'scores': [2, 3, 4, 3, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3]},
                 {'school_class': '1b', 'scores': [5, 5, 5, 4, 4, 5, 4, 5, 4, 4, 5, 4, 5, 4, 4, 5]},
                 {'school_class': '5a', 'scores': [3, 5, 4, 4, 3, 4, 3, 5, 5, 4, 3, 4, 5, 2]},
                 {'school_class': '5b', 'scores': [5, 4, 3, 4, 5, 3, 4, 2, 4, 5, 4, 5, 3, 4, 3, 5, 4, 3, 4]}
                 ]


all_grades = []

for one_class in school_grades:
    average_class_grade = int(sum(one_class['scores']) / len(one_class['scores']))
    print('Average grade in {}: {}'.format(one_class['school_class'], average_class_grade))
    all_grades.append(one_class['scores'][0])
average_school_grade = int(sum(all_grades)/len(all_grades))
print('Average school grade: {}'.format(average_school_grade))