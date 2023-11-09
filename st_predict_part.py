import pandas as pd
import streamlit as st
import plotly.express as px

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


def section1():
    ### --- show the tables to the user --- By Majed
    st.info('**:blue[Table 1-1: Enrolled students in higher education for the past 15 years]**')
    st.dataframe(new_s)
    st.caption('______________________________________________')
    st.info('**:blue[Table 1-2: Graduated students in higher education for the past 15 years]**')
    st.dataframe(grad_s)
    st.caption('______________________________________________')

def section2():
    ### --- choices for the charts --- By Majed
    st.success('**:green[Please choose the criteria below for the chart]**')
    selected_state = st.selectbox('Select the state of the student:', all_s['state'].unique())
    selected_degree = st.selectbox('Select the degree of the student:', all_s['degree'].unique())
    selected_sex = st.selectbox('Select the sex of the student:', all_s['sex'].unique())
    filtered_data = all_s[
        (all_s['state'] == selected_state) &
        (all_s['degree'] == selected_degree) &
        (all_s['sex'] == selected_sex) 
    ]


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

def section3():
    ### --- start the prediction part --- By Majed
    ### --- input choices from the user --- By Majed
    st.error('**:red[Please choose the criteria below for the graduates prediction]**')
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
    st.subheader(f":orange[The number of expected graduation students according to the above criteria is = ] {result} students")

def main():
    ### --- Page introduction --- By Majed
    st.set_page_config(page_title='Students Prediction')
    st.caption('______________________________________________')
    st.subheader(':rainbow[Statistics of Enrolled and Graduated Students in Saudi Universities During the Past 15 Years :student:]')
    st.markdown('**STREAMLIT-PROJECT: DONE ® 2023 BY:** ***ALL 704 STUDENTS***')
    st.caption('______________________________________________')

    # Create buttons in the sidebar --- By Majed
    selected_section = st.sidebar.radio("Selection Part for the Students", 
                                         [":blue[Student data over 15 years]", 
                                         ":green[Charts for Students]", 
                                         ":red[Predicting graduates]"])

    # Display the selected section --- By Majed
    if selected_section == ":blue[Student data over 15 years]":
        section1()
    elif selected_section == ":green[Charts for Students]":
        section2()
    elif selected_section == ":red[Predicting graduates]":
        section3()

if __name__ == "__main__":
    main()
