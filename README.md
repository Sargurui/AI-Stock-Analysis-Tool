# 📈 **Stock Analysis Tool**

### 🚀 **Analyze Stock Fundamentals and Technical Indicators**

This **Streamlit** app fetches financial data and technical indicators (e.g., SMA, RSI, Bollinger Bands) for any stock ticker symbol and leverages **Google Gemini AI** to provide clear investment recommendations.

---

## 📝 **Features**
- **Stock Fundamentals**: Market Cap, P/E Ratio, EPS, Dividend Yield, and more.
- **Technical Analysis**: 50-Day SMA, 200-Day SMA, RSI, and Bollinger Bands.
- **AI Analysis**: Intelligent investment suggestions using Gemini AI.
- **User-Friendly**: Simple, interactive interface powered by Streamlit.

---

## 🛠️ **Setup Instructions**

Follow these simple steps to set up and run the project.

### **1. Clone the Repository**
```bash
git clone <repository-link>
cd StockAnalysisTool
```

---

### **2. Install Dependencies**

Install all required Python libraries with this command:
```bash
pip install -r requirements.txt
```

**Dependencies**:
- `streamlit` → For the interactive web interface.
- `yfinance` → Fetch stock data.
- `python-dotenv` → Load environment variables securely.
- `google-generativeai` → Connect to the Google Gemini API.

---

### **3. Configure the Gemini API**

1. Obtain your **Google Gemini API Key** from [Google AI Studio](https://ai.google.dev).
2. Create a `.env` file in the project root directory.
3. Add your API key:
   ```env
   GEMINI_API_KEY=YOUR_API_KEY
   ```

---

### **4. Run the App**

Launch the Streamlit app by running:
```bash
streamlit run app.py
```

---

## 📊 **How to Use the App**

1. **Enter a Stock Symbol**:
   - Example: `AAPL` (Apple), `TSLA` (Tesla), or `MSFT` (Microsoft).

2. **View Fundamental Data**:
   - Company Name, Market Cap, P/E Ratio, Revenue, etc.

3. **View Technical Indicators**:
   - Moving Averages (SMA 50, SMA 200), RSI, and Bollinger Bands.

4. **Get AI-Powered Insights**:
   - Google Gemini will analyze the data and provide investment advice:
     - *"Should you invest? Why or why not?"*

---


## 🧪 **Example Use Case**

1. Open the app.
2. Input:  
   ```text
   Ticker: AAPL
   ```
3. Output:  
   - **Fundamentals**: Market Cap, EPS, Dividend Yield, etc.  
   - **Technicals**: SMA 50, SMA 200, RSI = 62.4, Bollinger Bands.  
   - **AI Analysis**:  
     > "Apple shows strong fundamentals and steady technical indicators. Its RSI indicates it's neither overbought nor oversold. Consider investing for long-term growth."

---

## ✅ **Troubleshooting**

### **Q1: The app won't start!**
- Ensure Python is installed (version 3.8+).
- Install dependencies using:
  ```bash
  pip install -r requirements.txt
  ```

### **Q2: API Error: "Invalid Key"**
- Double-check your **GEMINI_API_KEY** in the `.env` file.

### **Q3: No Data Found**
- Verify the stock ticker symbol (e.g., use `AAPL`, not `apple`).

---

## 💡 **Tips**

- Use stock symbols for global companies, like:
  - `AAPL` → Apple  
  - `TSLA` → Tesla  
  - `MSFT` → Microsoft  
  - `GOOG` → Alphabet  
- Experiment with different stocks and compare results.

---

## 🤝 **Contributing**

We welcome contributions! Here’s how you can help:
1. **Fork the repository.**
2. **Create a feature branch:**
   ```bash
   git checkout -b feature-name
   ```
3. **Commit your changes:**
   ```bash
   git commit -m "Add feature XYZ"
   ```
4. **Push and open a Pull Request.**


### 🌟 **Enjoy the app and happy investing!** 🌟
