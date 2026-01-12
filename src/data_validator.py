def validate_student_data(df):
    """
    Validate the structure and value ranges of student academic data.

    This function performs basic validation checks on a Pandas DataFrame
    containing student academic information. It is intended as a
    prototype-level validation module, not production-ready code.

    -----------------------
    INPUT
    -----------------------
    df : pandas.DataFrame
        A DataFrame expected to contain the following columns:
        - Attendance_Percentage : float or int (0 to 100)
        - Internal_Marks        : float or int (0 to 100)
        - Assignment_Score     : float or int (0 to 100)

    -----------------------
    OUTPUT
    -----------------------
    bool
        - True  : if the dataset passes all validation checks
        - False : if any validation rule fails

    -----------------------
    VALIDATION CHECKS
    -----------------------
    1. DataFrame existence (None check)
    2. Required column presence
    3. Empty DataFrame handling
    4. Missing (NaN) value detection
    5. Numeric data type validation
    6. Valid range checks for each column

    -----------------------
    NOTES
    -----------------------
    - This is a prototype validation function, intended for academic
      and internship projects.
    - Error handling is done via print statements for clarity.
    - No exceptions are raised to keep the flow simple and readable.
    """

    # Check if DataFrame exists
    if df is None:
        print("Validation failed: DataFrame is None")
        return False

    # Check for empty DataFrame
    if df.empty:
        print("Validation failed: DataFrame is empty")
        return False

    # Required columns
    required_columns = [
        "Attendance_Percentage",
        "Internal_Marks",
        "Assignment_Score"
    ]

    # Column existence check
    for col in required_columns:
        if col not in df.columns:
            print(f"Validation failed: Missing column -> {col}")
            return False

    # Missing value (NaN) check
    if df[required_columns].isnull().any().any():
        print("Validation failed: Missing values detected")
        return False

    # Data type and range validation
    for col in required_columns:
        # Ensure numeric data
        if not df[col].apply(lambda x: isinstance(x, (int, float))).all():
            print(f"Validation failed: Non-numeric values in {col}")
            return False

        # Ensure valid range
        if not df[col].between(0, 100).all():
            print(f"Validation failed: {col} values out of range (0-100)")
            return False

    # All checks passed
    print("Data validation successful")
    return True
