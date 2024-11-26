# Student Timetable Generator App

This Streamlit app helps students create a personalized daily timetable by inputting their subjects, study hours, and break durations. The app generates a structured timetable and allows users to download it as a CSV file for easy reference.

---

## Features

1. **Subject Input**:  
   Enter the subjects you want to study for the day.
   
2. **Study Hour Allocation**:  
   Specify the number of hours you want to dedicate to each subject.

3. **Break Customization**:  
   Adjust the break duration between study sessions.

4. **Timetable Generation**:  
   Automatically generates a structured timetable with start and end times for each subject.

5. **CSV Export**:  
   Download the generated timetable as a CSV file for easy sharing and printing.

---

## Installation

Follow these steps to set up and run the app locally:

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Install Dependencies
Ensure you have Python 3.8 or higher installed. Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 3. Run the App
Start the Streamlit server:
```bash
streamlit run student_timetable_app.py
```

### 4. Open in Browser
The app will open in your default web browser at:
```
http://localhost:8501
```

---

## How to Use

1. **Input Subjects**:  
   Enter the subjects you want to include in your timetable, separated by commas.  
   Example: `Math, Science, English`

2. **Enter Study Hours**:  
   Input the study hours for each subject, separated by commas.  
   Example: `2, 1.5, 1`

3. **Set Break Duration**:  
   Use the slider to select the desired break duration between study sessions (5–60 minutes).

4. **Generate Timetable**:  
   Click the **Generate Timetable** button to create your timetable.

5. **Download CSV**:  
   Use the **Download Timetable as CSV** button to save the timetable to your device.

---

## Example Timetable

| Subject   | Start Time | End Time |
|-----------|------------|----------|
| Math      | 08:00 AM   | 10:00 AM |
| Science   | 10:15 AM   | 11:45 AM |
| English   | 12:00 PM   | 01:00 PM |

---

## Requirements

- Python 3.8 or higher
- Required Python libraries:
  - `streamlit`
  - `pandas`

Install them using:
```bash
pip install -r requirements.txt
```

---

## Future Enhancements

- Allow users to input preferred start and end times.
- Add priority levels for subjects.
- Include visualizations, such as pie charts or Gantt charts.
- Enable timetable storage and retrieval for long-term planning.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

Developed by Mahpara Siddique. Contributions and feedback are always welcome!
