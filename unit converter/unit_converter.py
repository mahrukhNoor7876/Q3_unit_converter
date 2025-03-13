import streamlit as st;

st.title("🌏 Unit Converter App!")
st.markdown("This Unit Converter coverts the unit of length, mass, time and temperature accordingly")
st.write("Fill out the input fields and get the results!")

#Array of category
category = ["Length", "Mass", "Time", "Temperature"]

#function to convert unit of length
def convert_length(number_input, convert_from, convert_to):
    factors = {
        "meter": 1,
        "kilometer": 1000,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "micrometer": 0.000001
    }
    return number_input * factors[convert_from]/factors[convert_to]

#function to convert unit of mass
def convert_mass(number_input, convert_from, convert_to):
    factors = {
        "kilogram": 1,
        "gram": 1000,
        "pound": 2.205,
    }
    in_kg = number_input / factors[convert_from]
    return in_kg * factors[convert_to]

#function to convert unit of mass
def convert_time(number_input, convert_from, convert_to):
    factors = {
        "second": 1,
        "minute": 60,
        "hour": 3600
    }
    return number_input * factors[convert_from]/factors[convert_to]

#function to convert unit of temperature
def convert_temp(number_input, convert_from, convert_to):
    #if from unit is celsius
    if(convert_from == "Celsius"):
        if(convert_to == "Celsius"):
            return number_input
        elif(convert_to == "Fahrenheit"):
            return (number_input * 9/5) + 32
        elif(convert_to == "Kelvin"):
            return number_input + 273.15
        
    #if from unit is Fahrenheit    
    elif(convert_from == "Fahrenheit"):
        if(convert_to == "Fahrenheit"):
            return number_input
        elif(convert_to == "Celsius"):
            return (number_input - 32) * 5/9
        elif(convert_to == "Kelvin"):
            return (number_input - 32) * 5/9 + 273.15
        
    #if from unit is Kelvin
    elif(convert_from == "Kelvin"):
        if(convert_to == "Kelvin"):
            return number_input
        elif(convert_to == "Celsius"):
            return number_input - 273.15
        elif(convert_to == "Fahrenheit"):
            return (number_input - 273.15) * 9/5 + 32

#User interface
#provides options for category
selected_category = st.selectbox(
    "Select Category: ",
    category
)

#taking input
number_input = st.number_input("Enter the value: ")

#if length is selected
if(selected_category == "Length"):
    options = ["meter", "kilometer", "centimeter", "milimeter", "micrometer"]

#if mass is selected
elif(selected_category == "Mass"):
    options = ["kilogram", "gram", "pound"]

#if time is selected
elif(selected_category == "Time"):
    options = ["second", "minute", "hour"]

#if temperature is selected
elif(selected_category == "Temperature"):
    options = ["Celsius", "Fahrenheit", "Kelvin"]

else:
    st.write("Select Option!")

col1, col2 = st.columns(2)

#option from which unit is converted
with col1:
    convert_from = st.selectbox(
        "Convert from: ",
        options
    )

#option to which unit is converted
with col2:
    convert_to = st.selectbox(
        "Convert to: ",
        options
    )

#button
convert = st.button("Convert")

#if button is presed
if(convert == True):
    #calling functions
    if(selected_category == "Length"):
        result = convert_length(number_input, convert_from, convert_to)

    elif(selected_category == "Mass"):
        result = convert_mass(number_input, convert_from, convert_to)

    elif(selected_category == "Time"):
        result = convert_time(number_input, convert_from, convert_to)

    elif(selected_category == "Temperature"):
        result = convert_temp(number_input, convert_from, convert_to)

    #print the result
    st.success(f"Converted Value: {result} {convert_to}")