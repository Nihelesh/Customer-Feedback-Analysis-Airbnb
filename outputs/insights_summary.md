# Airbnb Guest Experience – Insights Summary

## Executive Summary
This analysis examines large-scale Airbnb customer reviews to identify drivers of guest dissatisfaction and surface actionable product and operational insights. By reframing sentiment into **Positive vs Non-Positive guest experiences** and combining NLP-based topic modeling with time-series and listing-level analysis, the project highlights key risk areas that impact customer satisfaction at scale.

---

## Overall Sentiment Health
- Approximately **80%** of English reviews reflect clearly positive guest experiences.
- Around **20%** of reviews fall into the **Non-Positive** category, representing guests at risk of dissatisfaction, churn, or negative word-of-mouth.
- Given Airbnb’s review positivity bias, this non-positive segment is large enough to warrant focused investigation.

---

## Key Experience Themes Identified
Topic modeling (LDA) revealed five dominant experience themes across reviews:

1. **Overall Positive Stay Experience**
2. **City-Center Accommodation**
3. **Memorable Airbnb Experience**
4. **Location & Walkability**
5. **Room Size & Amenities**

These topics capture both emotional and functional aspects of guest experiences.

---

## Topic-Level Risk Analysis
Analyzing the **Non-Positive rate within each topic** revealed significant variation in dissatisfaction risk:

- **Room Size & Amenities** shows the **highest risk**, with nearly **40%** of reviews in this topic being non-positive.
- **City-Center Accommodation** has the second-highest dissatisfaction rate (~32%), indicating expectation mismatches related to noise, space, and price.
- **Location & Walkability** and **Overall Stay Experience** are relatively low-risk topics and represent platform strengths.

### Key Insight
High-volume topics are not necessarily high-risk. Topics with structural constraints (space, amenities, accessibility) drive disproportionate dissatisfaction even when overall sentiment remains positive.

---

## Time-Based Risk Trends
Monthly trend analysis of Non-Positive sentiment shows that:
- Guest dissatisfaction fluctuates over time rather than remaining constant.
- Spikes in Non-Positive ratios can serve as **early-warning signals**, potentially correlating with seasonal demand, pricing changes, or policy updates.

This enables proactive monitoring of platform health beyond raw review volume.

---

## Listing-Level Risk Detection
A small number of listings generate a **disproportionately large number of non-positive reviews**:
- The top 10 problematic listings account for hundreds of dissatisfied guest experiences.
- These listings represent high-impact intervention opportunities for trust, safety, and operations teams.

### Key Insight
Targeted action on a small subset of high-risk listings can significantly reduce overall dissatisfaction and support operational efficiency.

---

## Qualitative Validation (Customer Voice)
Manual inspection of non-positive and negative reviews confirms that dissatisfaction is primarily driven by:
- Unexpectedly small rooms or difficult layouts
- Cleanliness and hygiene issues
- Poor accessibility or misleading location descriptions
- Pricing and value mismatches
- Operational friction (e.g., check-in problems)

Representative customer quotes were extracted to validate and humanize quantitative findings.

---

## Business Implications
- **Expectation management** is a major lever for improving satisfaction.
- Transparency around room size, accessibility, and amenities should be prioritized.
- City-center listings require clearer communication to align price, space, and experience expectations.
- Monitoring non-positive sentiment trends can inform proactive product and policy decisions.

---

## Limitations
- Analysis is limited to English-language reviews for linguistic consistency.
- Topic modeling relies on probabilistic word patterns and requires human interpretation.

---

## Conclusion
This project demonstrates how large-scale customer feedback can be transformed into actionable product insights using NLP and analytics. By shifting focus from raw sentiment counts to **risk-based dissatisfaction analysis**, the approach enables more effective prioritization, targeted interventions, and data-informed decision-making for customer experience improvement.

