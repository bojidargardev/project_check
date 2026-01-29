import streamlit as st

st.title("Мини тест – 3 проверки")

love_python = st.radio(
    "Обичаш ли Python?",
    ("да", "не")
)

number = st.number_input("Въведи число", step=1)

answer = st.number_input("Колко е 5 × 5?", step=1)

if st.button("Провери"):
    
    points = 0

    if love_python == "да":
        st.success("Верен отговор")
        points += 1
    else:
        st.error("Грешен отговор")

    if number > 10:
        st.success("Верен отговор")
        points += 1
    else:
        st.error("Грешен отговор")

    if answer == 25:
        st.success("Верен отговор")
        points += 1
    else:
        st.error("Грешен отговор")

    st.write("Резултат:", points, "/ 3")
