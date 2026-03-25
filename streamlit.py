import streamlit as st

# Fibonacci function
def fibonacci(n: int) -> list:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_seq = [0, 1]
    for _ in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq


# Streamlit UI
st.set_page_config(page_title="Fibonacci Generator", page_icon="🔢")

st.title("🔢 Fibonacci Sequence Generator")

st.write("Enter a number to generate Fibonacci sequence")

# Input
num = st.number_input("Number of terms", min_value=0, step=1)

# Button
if st.button("Generate"):
    result = fibonacci(num)

    if result:
        st.success("Fibonacci sequence generated!")
        st.write(result)
    else:
        st.warning("Please enter a number greater than 0")
