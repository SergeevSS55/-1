grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
studen_list = list(students)
studen_list.sort()
print(studen_list)
Aaron_average = sum(grades[0]) / len(grades[0])
Bilbo_average = sum(grades[1]) / len(grades[1])
Johny_average = sum(grades[2]) / len(grades[2])
Khendrik_average = sum(grades[3]) / len(grades[3])
Steve_average = sum(grades[4]) / len(grades[4])

dictionary_average = {studen_list[0] : Aaron_average,
                      studen_list[1] : Bilbo_average,
                      studen_list[2] : Johny_average,
                      studen_list[3] : Khendrik_average,
                      studen_list[4] : Steve_average}
print(dictionary_average)