import pandas as pd
import matplotlib.pyplot as plt

# Import functions from src package
from src.data_loader import load_student_data
from src.data_validator import validate_student_data
from src.data_cleaner import clean_student_data
from src.risk_labeling import assign_risk_level
from src.feature_engineering import feature_engineering
from src.ml_prediction import ml_predict_dropout_probability


def main():
    # Load the student data CSV
    data_path = "data/student_academic_data.csv"
    df = load_student_data(data_path)

    # Validate the data
    is_valid = validate_student_data(df)

    if not is_valid:
        print("Data is invalid. Exiting the program.")
        return
    
    # Display first few rows
    print(df.head())

    # Clean the data
    df, report = clean_student_data(df, min_attendance=75)
    print("Data is ready for analysis")
    print("Cleaning report:", report)

    # After cleaning, validation, and risk labeling
    df = feature_engineering(df, normalize=False)

    print("Feature engineering complete. Sample data:\n")

    # After cleaning and feature engineering
    df = assign_risk_level(df)
    # Check first few rows
    print(df.head())   

    # Plot risk distribution
    # df has 'Risk_Level' column
    risk_counts = df['Risk_Level'].value_counts()
    total_students = risk_counts.sum()

    ax = risk_counts.plot(kind='bar', color=['red', 'orange', 'green'])
    plt.xlabel("Risk Level")
    plt.ylabel("Number of Students")
    plt.title("Distribution of Students by Academic Risk Level")
    plt.xticks(rotation=0)

    # Add percentage labels on top of each bar
    for p in ax.patches:
        count = p.get_height()
        percentage = (count / total_students) * 100
        ax.annotate(f'{percentage:.1f}%', (p.get_x() + p.get_width() / 2., count),
                    ha='center', va='bottom', fontsize=10)
    plt.tight_layout()
    plt.savefig('risk_level_distribution.png')

    # ML Prediction
    # Create normalized ML dataset
    df_ml = feature_engineering(df, normalize=True)

    # Create target column
    df_ml['Pass_Fail'] = df_ml['Risk_Level'].apply(
        lambda x: 1 if x != 'High' else 0
    )

    # Feature columns
    feature_cols = [
        'Attendance_Percentage',
        'Internal_Marks',
        'Assignment_Score',
        'Total_Score',
        'Average_Score'
    ]

    # Train ML model and get dropout probability
    model, dropout_prob, test_index = ml_predict_dropout_probability(
        df_ml,
        feature_cols=feature_cols,
        target_col='Pass_Fail'
    )

    # Store probabilities only for test rows
    df_ml.loc[test_index, 'Dropout_Probability'] = dropout_prob.round(3)

    print("Dropout probability added successfully")
    print(df_ml[['Student_ID', 'Risk_Level', 'Dropout_Probability']].head())

    # Dropout Probability Distribution
    # identify how dropout risk isspread across students and 
    # enables early intervention for high-risk groups

    # Drop rows without dropout probability (training rows)
    plot_df = df_ml.dropna(subset=['Dropout_Probability'])

    plt.figure()
    plt.hist(plot_df['Dropout_Probability'], bins=10)
    plt.title('Distribution of Student Dropout Probability')
    plt.xlabel('Dropout Probability')
    plt.ylabel('Number of Students')
    plt.axvline(0.5, color='red', linestyle='dashed', linewidth=1)
    plt.text(0.52, plt.ylim()[1]*0.9, 'Threshold (0.5)', color='red')
    plt.tight_layout()
    plt.savefig('dropout_probability_distribution.png')

if __name__ == "__main__":
    main()
