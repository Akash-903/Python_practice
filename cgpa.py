import streamlit as st

# Title
st.title("📘 CGPA Calculator")

# User input: number of subjects
subjects = st.number_input("Enter Number of Subjects:", min_value=1, max_value=20, step=1)

grades = []
credits = []

# Collect grade points and credits
for i in range(int(subjects)):
    grade = st.number_input(f"Enter Grade Point for Subject {i+1} (0-10):", min_value=0.0, max_value=10.0, step=0.1, key=f"g{i}")
    credit = st.number_input(f"Enter Credits for Subject {i+1}:", min_value=1, max_value=10, step=1, key=f"c{i}")
    grades.append(grade)
    credits.append(credit)

# Calculate CGPA
def calculate_cgpa(grades, credits):
    total_credits = sum(credits)
    weighted_sum = sum(g * c for g, c in zip(grades, credits))
    return weighted_sum / total_credits if total_credits > 0 else 0

# Show results
if st.button("Calculate CGPA"):
    cgpa = calculate_cgpa(grades, credits)
    st.success(f"Your CGPA is: {cgpa:.2f}")
