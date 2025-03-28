import streamlit as st

import calculate_aqi
import calculate_aqi as calculate

# App Title
st.title('AQI Predictor')
st.subheader('Know the AQI by entering pollutant information')

col1, col2, col3 = st.columns(3)

# Form to take inputs
with col1:
    with st.form(key='inputs'):
        pm25 = st.number_input('Particulate Matter (PM2.5):', min_value=0, max_value=2000, step=1)
        pm10 = st.number_input('Particulate Matter (PM10):', min_value=0, max_value=2000, step=1)
        no2 = st.number_input('Nitrogen Dioxide (NO2):', min_value=0, max_value=2000, step=1)
        nh3 = st.number_input('Ammonia (NH3):', min_value=0, max_value=2000, step=1)
        so2 = st.number_input('Sulphur Dioxide (SO2):', min_value=0, max_value=2000, step=1)
        co = st.number_input('Carbon Monoxide (CO):', min_value=0, max_value=2000, step=1)
        o3 = st.number_input('Ozone (O3):', min_value=0, max_value=2000, step=1)

        submitted = st.form_submit_button('Submit')

with col2:
    st.write('### AQI Breakdown')

with col3:
    st.write('### Recommendations:')


# Run AQI calculation when the form is submitted
if submitted:
    pollutant_values = {"PM2.5": pm25, "PM10": pm10, "NO2": no2, "NH3": nh3, "SO2": so2, "CO": co, "O3": o3}
    aqi_values, final_aqi, category = calculate.compute_aqi(pollutant_values)

    with col2:
        # Display AQI for each pollutant
        for pollutant, value in aqi_values.items():
            st.write(f"- {pollutant}: **{round(value, 2)}**")

        st.write("## **AQI:**", int(final_aqi))
        st.subheader(f"Category: {category}")

    with col3:
        # Display recommendations
        if final_aqi <= 50:
            st.write('#### 😊 Enjoy outdoor activities without any restrictions')

        elif final_aqi <= 100:
            st.write('#### 🙂 Safe for most people; sensitive groups should limit prolonged exposure')

        elif final_aqi <= 200:
            st.write("#### 😐 Consider reducing outdoor exertion, especially if you have respiratory issues")

        elif final_aqi <= 300:
            st.write("#### 😷 Avoid outdoor activities; wear a mask if necessary")

        elif final_aqi <= 400:
            st.write("#### 🤢 Stay indoors as much as possible; use air purifiers if available")

        else:
            st.write("#### ☠️ Serious health risks; avoid going outside and ensure proper ventilation indoors")