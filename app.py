import streamlit as st
import pandas as pd

# Function to create a timetable
def create_timetable(subjects, study_hours, break_duration):
    total_time = sum(study_hours)
    timetable = []
    current_time = 8  # Starting time is 8:00 AM

    for i, subject in enumerate(subjects):
        start_time = current_time
        end_time = current_time + study_hours[i]
        timetable.append({
            "Subject": subject,
            "Start Time": f"{int(start_time)}:{int((start_time % 1) * 60):02d}",
            "End Time": f"{int(end_time)}:{int((end_time % 1) * 60):02d}"
        })
        current_time = end_time + (break_duration / 60)  # Add break time

    return pd.DataFrame(timetable)

# Streamlit app
st.title("Student Timetable Generator")
st.write("Plan your day effectively by creating a custom timetable.")

# Inputs
st.header("Input your preferences:")
subjects = st.text_input("Enter subjects (comma-separated):")
study_hours_input = st.text_input("Enter study hours per subject (comma-separated):")
break_duration = st.slider("Break duration between study sessions (minutes):", 5, 60, 15)

# Generate timetable
if st.button("Generate Timetable"):
    try:
        # Process inputs
        subjects_list = [s.strip() for s in subjects.split(",")]
        study_hours = [float(h.strip()) for h in study_hours_input.split(",")]

        # Validate inputs
        if len(subjects_list) != len(study_hours):
            st.error("Please ensure the number of subjects matches the number of study hours.")
        else:
            # Generate timetable
            timetable_df = create_timetable(subjects_list, study_hours, break_duration)
            st.success("Timetable created successfully!")
            st.dataframe(timetable_df)

            # Option to download timetable as CSV
            csv = timetable_df.to_csv(index=False)
            st.download_button(
                label="Download Timetable as CSV",
                data=csv,
                file_name="timetable.csv",
                mime="text/csv",
            )
    except ValueError:
        st.error("Invalid input! Please enter numeric values for study hours.")

