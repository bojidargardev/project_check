import streamlit as st

st.title("Мини тест")

answer_yes_no = st.radio(
    "Обичаш ли Python?",
    ("да", "не")
)

answer_math = st.number_input("Колко е 5 × 5?", step=1)

if st.button("Провери"):
    
    points = 0

    if answer_yes_no == "да":
        st.success("Верен отговор")
        points += 1
    else:
        st.error("Грешен отговор")

    if answer_math == 25:
        st.success("Верен отговор")
        points += 1
    else:
        st.error("Грешен отговор")

    st.write("Резултат:", points, "/ 2")
