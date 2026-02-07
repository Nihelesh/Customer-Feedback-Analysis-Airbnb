import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ============================
# Global Plot Styling (Very Compact)
# ============================
plt.rcParams.update({
    "figure.figsize": (4, 2.5),
    "font.size": 8,
    "axes.titlesize": 9,
    "axes.labelsize": 8
})

# ============================
# Page Config
# ============================
st.set_page_config(
    page_title="Airbnb Guest Experience Risk Dashboard",
    layout="wide"
)

st.title("🏡 Airbnb Guest Experience Risk Dashboard")
st.caption(
    "Monitoring guest dissatisfaction using NLP-based sentiment and topic analysis"
)

st.info(
    "ℹ️ Topics are generated using **LDA (unsupervised NLP)** and "
    "**manually interpreted and labeled by a human** based on keywords and review inspection."
)

# ============================
# Load Data
# ============================
@st.cache_data
def load_data():
    df = pd.read_csv("data/reviews_en_processed.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

# ============================
# Human-Interpreted Topic Labels
# ============================
TOPIC_LABELS = {
    0: "Overall Positive Stay Experience",
    1: "City-Center Accommodation",
    2: "Memorable Airbnb Experience",
    3: "Location & Walkability",
    4: "Room Size & Amenities"
}

df["topic_label"] = df["topic"].map(TOPIC_LABELS)

# ============================
# Display Topic Definitions
# ============================
st.markdown("## 🧠 Key Experience Themes Identified")

st.markdown(
    """
Topic modeling using **Latent Dirichlet Allocation (LDA)** revealed the following dominant
guest experience themes. These themes were **interpreted and labeled by a human**
to make them business-readable and actionable.
"""
)

theme_df = pd.DataFrame({
    "LDA Topic ID": TOPIC_LABELS.keys(),
    "Experience Theme (Human-Interpreted)": TOPIC_LABELS.values()
})

st.dataframe(theme_df, use_container_width=True)

# ============================
# Sidebar Filters
# ============================
st.sidebar.header("🔎 Filters")

# Date Filter
min_date = df["date"].min()
max_date = df["date"].max()

date_range = st.sidebar.date_input(
    "Select date range",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Topic Filter
topic_options = ["All"] + sorted(df["topic_label"].dropna().unique().tolist())
selected_topic = st.sidebar.selectbox("Select experience theme", topic_options)

# Listing Filter
listing_options = ["All"] + sorted(df["listing_id"].astype(str).unique().tolist())
selected_listing = st.sidebar.selectbox("Select listing", listing_options)

# ============================
# Apply Filters
# ============================
filtered_df = df.copy()

filtered_df = filtered_df[
    (filtered_df["date"] >= pd.to_datetime(date_range[0])) &
    (filtered_df["date"] <= pd.to_datetime(date_range[1]))
]

if selected_topic != "All":
    filtered_df = filtered_df[filtered_df["topic_label"] == selected_topic]

if selected_listing != "All":
    filtered_df = filtered_df[
        filtered_df["listing_id"].astype(str) == selected_listing
    ]

# ============================
# KPIs
# ============================
st.markdown("## 📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Reviews", f"{len(filtered_df):,}")

with col2:
    non_pos_rate = (filtered_df["sentiment_binary"] == "Non-Positive").mean() * 100
    st.metric("Non-Positive Rate", f"{non_pos_rate:.1f}%")

with col3:
    st.metric("Positive Rate", f"{100 - non_pos_rate:.1f}%")

with col4:
    st.metric("Unique Listings", filtered_df["listing_id"].nunique())

# ============================
# Sentiment Distribution
# ============================
st.markdown("## 🙂 Guest Sentiment Distribution")

sentiment_dist = (
    filtered_df["sentiment_binary"]
    .value_counts(normalize=True)
    .reindex(["Positive", "Non-Positive"]) * 100
)

fig, ax = plt.subplots(figsize=(4, 2.3))
ax.bar(sentiment_dist.index, sentiment_dist.values)
ax.set_ylabel("%")
ax.set_title("Positive vs Non-Positive")

st.pyplot(fig, use_container_width=False)

# ============================
# Trend Over Time
# ============================
st.markdown("## 📈 Non-Positive Experience Trend")

if len(filtered_df) > 0:
    monthly_risk = (
        filtered_df.groupby(filtered_df["date"].dt.to_period("M"))["sentiment_binary"]
        .value_counts(normalize=True)
        .unstack()
    )

    monthly_risk.index = monthly_risk.index.to_timestamp()

    fig, ax = plt.subplots(figsize=(5, 2.3))
    ax.plot(monthly_risk.index, monthly_risk["Non-Positive"])
    ax.set_ylabel("Non-Positive %")
    ax.set_xlabel("Date")
    ax.set_title("Monthly Dissatisfaction Trend")

    st.pyplot(fig, use_container_width=False)
else:
    st.warning("No data available for selected filters.")

# ============================
# Topic Risk Table
# ============================
st.markdown("## ⚠️ Topic-wise Risk Breakdown")

topic_risk = (
    filtered_df.groupby("topic_label")["sentiment_binary"]
    .value_counts(normalize=True)
    .unstack()
)

st.dataframe(
    topic_risk.style.format("{:.2%}"),
    use_container_width=True
)

# ============================
# High-Risk Listings
# ============================
st.markdown("## 🚨 High-Risk Listings")

problematic_listings = (
    filtered_df[filtered_df["sentiment_binary"] == "Non-Positive"]
    .groupby("listing_id")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

st.dataframe(
    problematic_listings.rename("Non-Positive Reviews"),
    use_container_width=True
)

# ============================
# Negative-Only Customer Feedback
# ============================
st.markdown("## 🔴 Negative Customer Feedback (Severe Issues)")

negative_reviews = filtered_df[
    filtered_df["sentiment_ml"] == "Negative"
]

if len(negative_reviews) > 0:
    sample_negative = negative_reviews.sample(
        min(5, len(negative_reviews)),
        random_state=42
    )

    for _, row in sample_negative.iterrows():
        st.markdown(
            f"""
            > **Listing {int(row['listing_id'])}**  
            > *“{row['comments']}”*  
            > _Theme: {row['topic_label']}_  
            """
        )
else:
    st.info("No negative reviews found for the selected filters.")
