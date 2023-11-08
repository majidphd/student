import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

### --- Page introduction --- By Majed
st.set_page_config(page_title='Students Prediction')
st.title('**:violet[________________________________]**')
st.title(':rainbow[Graduating Students Prediction :student: from Higher Education at KSA] :teacher: ')
st.title('**:violet[________________________________]**')
st.subheader('Done By: ***Majed, Hani, Ali, & Omar***')
st.caption('______________________________________________')

### --- load excel table --- By Majed
excel_file = 'student.xlsx'
sheet_name1 = 'data'
sheet_name2 = 'new'
sheet_name3 = 'grad'


### --- define table sheets --- By Majed
all_s = pd.read_excel(excel_file,
                                sheet_name=sheet_name1)
new_s = pd.read_excel(excel_file,
                                sheet_name=sheet_name2)
grad_s = pd.read_excel(excel_file,
                                sheet_name=sheet_name3)


### --- show the tables to the user --- By Majed
st.caption('**:blue[Table 1-1: Enrolled students in higher education for the past 15 years]**')
st.dataframe(new_s)
st.caption('______________________________________________')
st.caption('**:blue[Table 1-2: Graduated students in higher education for the past 15 years]**')
st.dataframe(grad_s)
st.caption('______________________________________________')


### --- sidebar choices for the charts --- By Majed
st.sidebar.title('***:green[Choices for the charts]***')
selected_state = st.sidebar.selectbox('Select the state of the student:', all_s['state'].unique())
selected_degree = st.sidebar.selectbox('Select the degree of the student:', all_s['degree'].unique())
selected_sex = st.sidebar.selectbox('Select the sex of the student:', all_s['sex'].unique())
filtered_data = all_s[
    (all_s['state'] == selected_state) &
    (all_s['degree'] == selected_degree) &
    (all_s['sex'] == selected_sex) 
]
st.sidebar.caption('____________________')
st.sidebar.title('***:red[for prediction part ROLL-DOWN in the main page]***')


### --- show the charts according to user choices --- By Majed
bar_chart = px.bar(filtered_data,
                   x='years',
                   y='numbers',
                   text='numbers',
                   color_discrete_sequence = ['#F63366']*len(all_s),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)
st.caption('______________________________________________')
pie_chart = px.pie(filtered_data,
                title='The ratio of students for 15 years',
                values='numbers',
                names='years')
st.plotly_chart(pie_chart)
st.title('**:violet[________________________________]**')

### --- start the prediction part --- By Majed
### --- input choices from the user --- By Majed
st.title(':rainbow[The Prediction Part ]:thinking_face:')
st.title('**:violet[________________________________]**')
selected_degree2 = st.selectbox('Select the degree of enrolled student:', all_s['degree'].unique())
selected_sex2 = st.selectbox('Select the sex of enrolled student:', all_s['sex'].unique())
write_number = st.number_input("Enter the number of enrolled students:")
st.caption('______________________________________________')

### --- state if conditions for the prediction --- By Majed
result = 0
if write_number == 0:
    st.subheader('**:red[You have to inter a positive number for enrolled students]**')
elif write_number <= 0:
    st.subheader('**:red[:smile:يا وااااااااد قووووووووم يا وااااااااد]**')
elif (selected_degree2 == "PhD" and selected_sex2 == "Male"):
    result = write_number * 0.1
elif (selected_degree2 == "PhD" and selected_sex2 == "Female"):
    result = write_number * 0.09
elif (selected_degree2 == "Master" and selected_sex2 == "Male"):
    result = write_number * 0.15
elif (selected_degree2 == "Master" and selected_sex2 == "Female"):
    result = write_number * 0.14
elif (selected_degree2 == "Diploma" and selected_sex2 == "Male"):
    result = write_number * 0.57
elif (selected_degree2 == "Diploma" and selected_sex2 == "Female"):
    result = write_number * 0.6
elif (selected_degree2 == "Bachelor" and selected_sex2 == "Male"):
    result = write_number * 0.11
elif (selected_degree2 == "Bachelor" and selected_sex2 == "Female"):
    result = write_number * 0.15
else:
    result = 0
st.subheader(f"**:orange[The expected number of graduation students are = ] {result}**")

