import streamlit as st
import numpy as np


def load_css():
    with open("style.css", "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)


def calculate(operation, num1, num2):
    if operation == "Add (+)":
        return num1 + num2
    elif operation == "Subtract (-)":
        return num1 - num2
    elif operation == "Multiply (×)":
        return num1 * num2
    elif operation == "Divide (÷)":
        return num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == "Power (^)":
        return np.power(num1, num2)
    else:
        return "Invalid Operation"


st.title("Simple Calculator")
load_css()

num1 = st.number_input("Enter first number", value=0.0, step=0.1)
num2 = st.number_input("Enter second number", value=0.0, step=0.1)
operation = st.selectbox("Choose an operation", ["Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)", "Power (^)"])

if st.button("Calculate"):
    result = calculate(operation, num1, num2)
    st.success(f"Result: {result}")