import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/vendor_data.csv")

print("\n===== DATASET PREVIEW =====")
print(df.head())

# Dataset Information
print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

# Missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Average Delivery Time
print("\n===== AVERAGE DELIVERY TIME =====")
print(df["Delivery_Time"].mean())

# Best Quality Vendor
best_quality = df.sort_values(by="Quality_Score", ascending=False)

print("\n===== BEST QUALITY VENDORS =====")
print(best_quality[["Vendor_Name", "Quality_Score"]])

# Reliability
reliable = df.sort_values(by="Reliability_Score", ascending=False)

print("\n===== MOST RELIABLE VENDORS =====")
print(reliable[["Vendor_Name", "Reliability_Score"]])

# Lowest Cost Vendor
low_cost = df.sort_values(by="Cost_per_Unit")

print("\n===== LOWEST COST VENDORS =====")
print(low_cost[["Vendor_Name", "Cost_per_Unit"]])

# Vendor Performance Score
df["Performance_Score"] = (
    df["Quality_Score"] * 0.4 +
    df["On_Time_Delivery"] * 0.3 +
    df["Reliability_Score"] * 0.2 -
    df["Defect_Rate"] * 0.1
)

top_vendor = df.sort_values(by="Performance_Score", ascending=False)

print("\n===== TOP VENDORS =====")
print(top_vendor[["Vendor_Name", "Performance_Score"]])

# Save report
df.to_csv("reports/final_vendor_report.csv", index=False)

print("\nReport Saved Successfully")

# ================= VISUALIZATIONS =================

# Delivery Time
plt.figure(figsize=(8,5))
sns.barplot(x="Vendor_Name", y="Delivery_Time", data=df)
plt.title("Vendor Delivery Time")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("reports/delivery_time_chart.png")
plt.close()

# Quality Score
plt.figure(figsize=(8,5))
sns.barplot(x="Vendor_Name", y="Quality_Score", data=df)
plt.title("Vendor Quality Score")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("reports/quality_score_chart.png")
plt.close()

# Reliability Score
plt.figure(figsize=(8,5))
sns.lineplot(x="Vendor_Name", y="Reliability_Score", data=df, marker='o')
plt.title("Vendor Reliability")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("reports/reliability_chart.png")
plt.close()

# Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("reports/correlation_heatmap.png")
plt.close()

print("\nCharts Generated Successfully")
