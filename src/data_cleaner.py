import pandas as pd

def clean_student_data(df,min_attendance=75
                       ):
    """
    Clean student academic data.

    This function performs cleaning on a Pandas DataFrame containing student information.
    It handles missing values, corrects invalid data, and ensures numeric columns are valid.

    -----------------------
    INPUT
    -----------------------
    df : pandas.DataFrame
        Expected columns:
        - Attendance_Percentage : float or int (0 to 100)
        - Internal_Marks        : float or int (0 to 100)
        - Assignment_Score      : float or int (0 to 100)

    -----------------------
    OUTPUT
    -----------------------
    tuple
        clean_df : pandas.DataFrame
            Cleaned DataFrame with missing values filled and out-of-range values corrected.
        error_report : dict
            Dictionary reporting corrections made during cleaning.
    """

    error_report = {}

    if df is None or df.empty:
        error_report['error'] = 'DataFrame is None or empty'
        return df, error_report

    required_columns = [
        "Attendance_Percentage",
        "Internal_Marks",
        "Assignment_Score"
    ]

    clean_df = df.copy()

    for col in required_columns:
        # Convert non-numeric values to numeric, invalids become NaN
        clean_df[col] = pd.to_numeric(clean_df[col], errors='coerce')

        # Handle missing values by filling with column mean
        missing_count = clean_df[col].isnull().sum()
        if missing_count > 0:
            error_report[f'{col}_missing_filled'] = missing_count
            clean_df[col].fillna(clean_df[col].mean(), inplace=True)

        # Clip values to valid range 0–100
        out_of_range_count = ((clean_df[col] < 0) | (clean_df[col] > 100)).sum()
        if out_of_range_count > 0:
            error_report[f'{col}_out_of_range_clipped'] = out_of_range_count
            clean_df[col] = clean_df[col].clip(0, 100)

    return clean_df, error_report
