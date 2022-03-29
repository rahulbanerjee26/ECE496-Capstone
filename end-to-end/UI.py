import streamlit as st 

st.set_page_config(
    page_title='Real Time PPG', 
    layout='wide', 
    initial_sidebar_state='collapsed'
)

sidebar = st.sidebar


page = sidebar.radio(label='Chose Page',options=['Home','Train','Test'])

if page == 'Home':
    st.markdown(''' 
    <h1> Plethysmograph for human biometric recognition </h1>

    <h2><u>Supervisor</u></h2>
    <h3> Dimitrios Hatzinakos </h3>

    <h2> <u> Team Members </u> </h2>
    <h3>
    <ul> Pratyush Menon </ul>
    <ul> Saminul Islam Samin </ul>
    <ul> Dhruv Patel </ul>
    <ul> Rahul Banerjee </ul>
    </h3>

    <h2> <u> About </u> </h2>
    <p>
    The goal of this project is to develop a method for using capacitive signals measured from human touch to provide biometric recognition and authentication. The project will use signal processing and machine learning techniques to denoise and analyze the measured capacitive signals to recognize the person to whom the signal belongs. It will also involve building a capacitive sensor which supports measuring signals from human touch and streaming them to a computing device on which the analysis can be performed.
    </p>

    <h2> <u> Steps for Real Time Authentication </u> </h2>
    <ul> 1. Collect your PPG Data for 90 seconds using the Bitalino PPG Device </ul>

    <ul> 2. Butterworth Filter will be applied to your Data. Following which it will be broken into intervals. Finally, each interval will be min-max normalized <ul>

    <ul> 3. The Authentication Model (which consists of a pre-trained Classifier Model) will be trained on your collected data </ul>

    <ul> 4. Use the PPG Device to measure your data again and test the Model </ul>
    ''',unsafe_allow_html=True)


if page == 'Train':
    st.title("Train Model on Your Data")


if page == 'Test':
    st.title("Test Trained Models")
