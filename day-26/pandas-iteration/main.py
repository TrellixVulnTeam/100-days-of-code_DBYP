student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Loop through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame:
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame:
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)
#     print(row.score)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)


