import pandas as pd

def feature_engineering(df, normalize=False):
    """
    Perform feature engineering on student academic data.

    This function creates new meaningful features from raw data:
    - Total Score
    - Average Score
    - Attendance Category (Low, Medium, High)
    - Optional normalization of numeric features

    -----------------------
    INPUT
    -----------------------
    df : pandas.DataFrame
        Columns required:
        - Attendance_Percentage
        - Internal_Marks
        - Assignment_Score
    normalize : bool, optional
        If True, scales numeric scores (Internal_Marks, Assignment_Score, Total_Score, Average_Score)
        to 0-1 range.

    -----------------------
    OUTPUT
    -----------------------
    df : pandas.DataFrame
        Original DataFrame with new features added:
        - Total_Score
        - Average_Score
        - Attendance_Category
        - Optionally normalized numeric columns
    """

    df = df.copy()

    # 1️ Total score
    df['Total_Score'] = df['Internal_Marks'] + df['Assignment_Score']

    # 2️ Average score
    df['Average_Score'] = df['Total_Score'] / 2

    # 3️ Attendance category
    def attendance_cat(att):
        if att < 75:
            return 'Low'
        elif att <= 85:
            return 'Medium'
        else:
            return 'High'

    df['Attendance_Category'] = df['Attendance_Percentage'].apply(attendance_cat)

    # 4️ Optional normalization
    if normalize:
        numeric_cols = ['Internal_Marks', 'Assignment_Score', 'Total_Score', 'Average_Score']
        for col in numeric_cols:
            min_val = df[col].min()
            max_val = df[col].max()
            if max_val - min_val > 0:
                df[col] = ((df[col] - min_val) / (max_val - min_val))
            else:
                df[col] = 0.0  # all values same, normalize to 0
            df[col] = df[col].round(3)

    return df
