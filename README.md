# Scalable NLP-Based Guest Experience Risk Detection on Airbnb Reviews

## 📌 Project Overview
Airbnb receives millions of customer reviews containing rich but unstructured feedback. Manually analyzing this feedback at scale is not feasible. This project builds an end-to-end NLP and product analytics pipeline to automatically identify guest satisfaction patterns, detect early dissatisfaction signals, and surface actionable insights for product and operations teams.

The system reframes traditional sentiment analysis into **Positive vs Non-Positive guest experience detection**, aligning more closely with real-world product risk monitoring.

---

## 🎯 Business Questions Addressed
- What experience areas drive guest dissatisfaction?
- Which topics are most associated with non-positive sentiment?
- Are guest experiences improving or degrading over time?
- Which listings generate repeated dissatisfaction and require intervention?

---

## 🧠 Key Concepts Used
- Natural Language Processing (NLP)
- Weakly Supervised Sentiment Learning
- Topic Modeling (LDA)
- Risk-Based Product Analytics
- Qualitative Validation using Customer Quotes

---

## 🏗️ Project Architecture

1. **Data Cleaning & Preparation**
   - Removed missing and invalid reviews
   - Normalized and cleaned text
   - Converted timestamps for time-based analysis

2. **Multilingual Handling**
   - Detected review language using `langdetect`
   - Filtered to English-only reviews for linguistic consistency
   - Documented multilingual support as future work

3. **Sentiment Analysis**
   - Rule-based sentiment as weak labels
   - TF-IDF + Logistic Regression for ML-based sentiment
   - Reframed sentiment into Positive vs Non-Positive for risk detection

4. **Topic Modeling**
   - LDA topic modeling using CountVectorizer
   - Sampling + online learning for scalability
   - Identified major experience themes such as:
     - Room Size & Amenities
     - City-Center Accommodation
     - Location & Walkability
     - Overall Stay Experience

5. **Product Risk Analytics**
   - Topic-wise non-positive rate analysis
   - Monthly trend monitoring of dissatisfaction
   - Listing-level risk detection

6. **Qualitative Validation**
   - Manual inspection of non-positive reviews
   - Extracted representative customer quotes to validate insights

---

## 📊 Key Insights
- ~20% of English reviews indicate non-positive guest experiences
- Room Size & Amenities and City-Center Accommodation topics show the highest dissatisfaction rates
- A small number of listings generate a disproportionate share of negative experiences
- Non-positive sentiment trends provide an early-warning system for product health

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib
- NLP (TF-IDF, LDA)
- langdetect

---

## ⚠️ Limitations & Ethics
- Reviews are naturally biased toward positive experiences
- Analysis is limited to English reviews for accuracy
- Insights should not be used to penalize hosts without human review

---

## 🚀 Future Improvements
- Multilingual sentiment modeling
- Transformer-based NLP (BERT)
- Real-time dashboards (Power BI / Tableau)
- Automated host intervention recommendations

---

## 👤 Author
Nihelesh

