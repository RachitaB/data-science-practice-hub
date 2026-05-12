import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    # Format: {'old_name': 'new_name'}
    students = students.rename(columns={'id':'student_id', 'first':'first_name',  'last':'last_name', 'age':'age_in_years'})
    return students