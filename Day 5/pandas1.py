import pandas as pd
import numpy as np
import openpyxl

technologies = ["Python", "Java", "JavaScript", "C++", "C#", "Go", "Rust", "Kotlin", "Swift", "Ruby", "Kotlin/Native",]
fee = [25000, 4000, 3000, 2000, 1500, 1000, 80]
duration = ['50 days', '30 days', np.nan, '15 days']
discount =[2000, 1500, 800, 1000, 500]
columns = ["Courses", "Fee", "Duration", "Discount"]

# wynik = dict(zip(columns, [technologies, fee, duration, discount]))
df = pd.DataFrame(list(zip(technologies, fee, duration, discount)), columns=columns)
# print(wynik)
print(df)

