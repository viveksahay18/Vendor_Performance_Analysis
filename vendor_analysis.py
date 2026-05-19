import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("data/vendor_data.csv")

print(df.head())
print(df.info())

print(df.describe())

print(df.isnull().sum())
df = df.dropna()
df = df.drop_duplicates()
print("Average Delivery Time:")
print(df["Delivery_Time"].mean())
best_quality = df.sort_values(by="Quality_Score", ascending=False)

print(best_quality[["Vendor_Name", "Quality_Score"]])
reliable = df.sort_values(by="Reliability_Score", ascending=False)

print(reliable[["Vendor_Name", "Reliability_Score"]])
low_cost = df.sort_values(by="Cost_per_Unit")

print(low_cost[["Vendor_Name", "Cost_per_Unit"]])
plt.figure(figsize=(8,5))

sns.barplot(x="Vendor_Name", y="Delivery_Time", data=df)

plt.title("Vendor Delivery Time")
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(8,5))

sns.barplot(x="Vendor_Name", y="Quality_Score", data=df)

plt.title("Vendor Quality Score")
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(8,5))

sns.lineplot(x="Vendor_Name", y="Reliability_Score", data=df, marker='o')

plt.title("Vendor Reliability")
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(10,6))

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="Blues")

plt.title("Correlation Heatmap")
plt.show()
df["Performance_Score"] = (
    df["Quality_Score"] * 0.4 +
    df["On_Time_Delivery"] * 0.3 +
    df["Reliability_Score"] * 0.2 -
    df["Defect_Rate"] * 0.1
)
top_vendor = df.sort_values(by="Performance_Score", ascending=False)

print(top_vendor[["Vendor_Name", "Performance_Score"]])
df.to_csv("reports/final_vendor_report.csv", index=False)

print("Report Saved Successfully")


