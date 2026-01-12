def assign_risk_level(df):
    """
    Assign academic risk levels based on attendance, internal marks, and assignment scores.

    Rules:
        - High Risk: Attendance < 75 or Internal_Marks < 50
        - Medium Risk: Attendance 75-85 or Internal_Marks 50-70
        - Low Risk: Attendance > 85 and Internal_Marks > 70

    INPUT:
        df : pandas.DataFrame
            Cleaned student data

    OUTPUT:
        df : pandas.DataFrame
            Adds 'Risk_Level' column
    """
    def risk(row):
        if row['Attendance_Percentage'] < 75 or row['Internal_Marks'] < 50:
            return 'High'
        elif row['Attendance_Percentage'] <= 85 or row['Internal_Marks'] <= 70:
            return 'Medium'
        else:
            return 'Low'

    df['Risk_Level'] = df.apply(risk, axis=1)
    return df
