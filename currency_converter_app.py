# currency_converter_app.py

import streamlit as st

def main():
    st.title("💱 Currency Converter (INR Based)")
    st.write("Convert Indian Rupees into currencies of different countries.")

    currency = st.selectbox("Select conversion:", [
        "INR to US Dollar",
        "INR to Pound",
        "INR to Euro",
        "INR to Dirham (AED)",
        "INR to Won (KRW)",
        "INR to Yen (JPY)",
        "INR to Ruble",
        "INR to Chinese Yuan",
        "INR to Turkish Lira"
    ])

    amount = st.number_input("Enter amount in INR:", min_value=0.0, format="%.2f")

    if st.button("Convert"):
        if amount <= 0:
            st.warning("Please enter a valid amount!")
        else:
            if currency == "INR to US Dollar":
                result = amount * 0.013
                st.success(f"{amount} INR = {result:.3f} USD")
            elif currency == "INR to Pound":
                result = amount * 0.010
                st.success(f"{amount} INR = {result:.3f} Pounds")
            elif currency == "INR to Euro":
                result = amount * 0.012
                st.success(f"{amount} INR = {result:.3f} Euros")
            elif currency == "INR to Dirham (AED)":
                result = amount * 0.046
                st.success(f"{amount} INR = {result:.3f} AED")
            elif currency == "INR to Won (KRW)":
                result = amount * 16.45
                st.success(f"{amount} INR = {result:.3f} Won")
            elif currency == "INR to Yen (JPY)":
                result = amount * 1.73
                st.success(f"{amount} INR = {result:.3f} Yen")
            elif currency == "INR to Ruble":
                result = amount * 0.72
                st.success(f"{amount} INR = {result:.3f} Ruble")
            elif currency == "INR to Chinese Yuan":
                result = amount * 0.085
                st.success(f"{amount} INR = {result:.3f} Yuan")
            elif currency == "INR to Turkish Lira":
                result = amount * 0.22
                st.success(f"{amount} INR = {result:.3f} Lira")

if __name__ == "__main__":
    main()
