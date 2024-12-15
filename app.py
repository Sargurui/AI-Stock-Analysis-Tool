import streamlit as st
from data_fetcher import get_company_data, get_technical_analysis
from analysis import generate_response, chat_session

st.title("AI Stock Analysis Tool")

# Input ticker symbol
ticker = st.text_input("Enter the stock ticker symbol (e.g., AAPL, TSLA):")

if ticker:
    # Step 1: Fetch company data
    st.subheader("Fetching Company Data...")
    company_data = get_company_data(ticker.upper())

    if company_data:
        # Step 2: Fetch technical analysis
        st.subheader("Fetching Technical Analysis...")
        technical_data = get_technical_analysis(ticker.upper())

        if technical_data:
            # Combine data for Gemini analysis
            combined_data = {**company_data, **technical_data}

            # Step 3: Generate Gemini response
            query = "Analyze the company's fundamentals and technical indicators and recommend whether to invest."
            st.subheader("Generating Investment Analysis...")
            response = generate_response(query, combined_data, chat_session.history)

            # Step 4: Display analysis
            st.write("### Investment Analysis:")
            st.write(response)
        else:
            st.error("Could not fetch technical analysis data.")
    else:
        st.error("Could not fetch company data. Please check the ticker symbol.")
