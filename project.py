import numpy as np
import pandas as pd

# Load the Student Marks dataset
df = pd.read_csv('Student_Marks.csv')

print("Original Dataset:")
print(df.head(10))

# 1. Remove duplicate records
df = df.drop_duplicates(keep='first')

# 2. Clean Number of Courses
df['number_courses'] = pd.to_numeric(
    df['number_courses'], errors='coerce'
)

df.loc[
    (df['number_courses'] < 1) |
    (df['number_courses'] > 20),
    'number_courses'
] = np.nan

median_courses = df['number_courses'].median()

df['number_courses'] = df['number_courses'].fillna(
    median_courses
).round().astype(int)

# 3. Clean Study Time
df['time_study'] = pd.to_numeric(
    df['time_study'], errors='coerce'
)

df.loc[
    (df['time_study'] < 0) |
    (df['time_study'] > 24),
    'time_study'
] = np.nan

df['time_study'] = df['time_study'].fillna(
    df['time_study'].median()
)

# 4. Clean Marks
df['Marks'] = pd.to_numeric(
    df['Marks'], errors='coerce'
)

df.loc[
    (df['Marks'] < 0) |
    (df['Marks'] > 100),
    'Marks'
] = np.nan

df['Marks'] = df['Marks'].fillna(
    df['Marks'].median()
)

# 5. Export cleaned dataset
df.to_csv('cleaned_Student_Marks.csv', index=False)

print("\nCleaned Dataset:")
print(df.head(10))

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nCleaned dataset saved successfully!")