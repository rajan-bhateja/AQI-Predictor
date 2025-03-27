import streamlit as st
import calculate_aqi as calculate

# App Title
st.title('AQI Predictor')
st.subheader('Know the AQI by entering pollutant information')
st.divider()

col1, col2 = st.columns(2)

# Form to take inputs
with col1:
    with st.form(key='inputs'):
        st.subheader('Enter Pollutants Values:')
        pm25 = st.number_input('PM2.5:', min_value=0, max_value=2000, step=1)
        pm10 = st.number_input('PM10:', min_value=0, max_value=2000, step=1)
        no2 = st.number_input('NO2:', min_value=0, max_value=2000, step=1)
        nh3 = st.number_input('NH3:', min_value=0, max_value=2000, step=1)
        so2 = st.number_input('SO2:', min_value=0, max_value=2000, step=1)
        co = st.number_input('CO:', min_value=0, max_value=2000, step=1)
        o3 = st.number_input('O3:', min_value=0, max_value=2000, step=1)

        submitted = st.form_submit_button('Submit')

# Run AQI calculation when the form is submitted
if submitted:
    pollutant_values = {"PM2.5": pm25, "PM10": pm10, "NO2": no2, "NH3": nh3, "SO2": so2, "CO": co, "O3": o3}
    aqi_values, final_aqi, category = calculate.compute_aqi(pollutant_values)

    with col2:
        # Display AQI for each pollutant
        st.write("### AQI Breakdown:")
        for pollutant, value in aqi_values.items():
            st.write(f"- {pollutant}: **{round(value, 2)}**")

        # Display final AQI
        if final_aqi <= 50:
            st.write('Good')
        elif final_aqi <= 100:
            st.write('Satisfactory')
        elif final_aqi <= 200:
            st.write('Moderate')
        elif final_aqi <= 300:
            st.write('Poor')
        elif final_aqi <= 400:
            st.write('Very Poor')
        else:
            st.write('Severe')

        st.write("## **Final AQI:**", round(final_aqi, 2))

        if category=='Good':
            st.subheader('Good')
        st.subheader(f"AQI Category: {category}")
