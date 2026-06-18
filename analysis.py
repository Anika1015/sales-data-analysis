import pandas as pd
import matplotlib.pyplot as plt

# ── Load Data ──────────────────────────────────────────────────────────────────
df = pd.read_csv("sales.csv")
print(f"Dataset loaded! {len(df)} rows, {len(df.columns)} columns\n")

# ── Chart 1: Total Sales by Product Category ──────────────────────────────────
plt.figure(figsize=(10, 5))
df.groupby("product_category")["total_price"].sum().sort_values().plot(
    kind="barh", color="steelblue")
plt.title("Total Sales by Product Category", fontsize=14, fontweight="bold")
plt.xlabel("Total Sales ($)")
plt.tight_layout()
plt.savefig("chart1_sales_by_category.png")
plt.show()
print("Chart 1 saved: Sales by Product Category")

# ── Chart 2: Total Sales by Branch ────────────────────────────────────────────
plt.figure(figsize=(7, 5))
df.groupby("branch")["total_price"].sum().plot(
    kind="bar", color=["#2e75b6", "#e74c3c", "#27ae60"], edgecolor="white")
plt.title("Total Sales by Branch", fontsize=14, fontweight="bold")
plt.xlabel("Branch")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart2_sales_by_branch.png")
plt.show()
print("Chart 2 saved: Sales by Branch")

# ── Chart 3: Customer Type Distribution ───────────────────────────────────────
plt.figure(figsize=(6, 6))
df["customer_type"].value_counts().plot(
    kind="pie", autopct="%1.1f%%",
    colors=["#3498db", "#e74c3c"],
    startangle=90)
plt.title("Customer Type: Member vs Normal", fontsize=14, fontweight="bold")
plt.ylabel("")
plt.tight_layout()
plt.savefig("chart3_customer_type.png")
plt.show()
print("Chart 3 saved: Customer Type Distribution")

# ── Chart 4: Sales by Gender ───────────────────────────────────────────────────
plt.figure(figsize=(6, 5))
df.groupby("gender")["total_price"].sum().plot(
    kind="bar", color=["#9b59b6", "#1abc9c"], edgecolor="white")
plt.title("Total Sales by Gender", fontsize=14, fontweight="bold")
plt.xlabel("Gender")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart4_sales_by_gender.png")
plt.show()
print("Chart 4 saved: Sales by Gender")

# ── Chart 5: Top 10 Best Selling Products ─────────────────────────────────────
plt.figure(figsize=(10, 6))
df.groupby("product_name")["quantity"].sum().sort_values(ascending=False).head(10).plot(
    kind="bar", color="darkorange", edgecolor="white")
plt.title("Top 10 Best Selling Products (by Quantity)", fontsize=14, fontweight="bold")
plt.xlabel("Product")
plt.ylabel("Total Quantity Sold")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("chart5_top_products.png")
plt.show()
print("Chart 5 saved: Top 10 Products")

# ── Chart 6: Sales by City ─────────────────────────────────────────────────────
plt.figure(figsize=(8, 5))
df.groupby("city")["total_price"].sum().sort_values(ascending=False).plot(
    kind="bar", color="#2e75b6", edgecolor="white")
plt.title("Total Sales by City", fontsize=14, fontweight="bold")
plt.xlabel("City")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("chart6_sales_by_city.png")
plt.show()
print("Chart 6 saved: Sales by City")

# ── Key Insights ───────────────────────────────────────────────────────────────
print("\n" + "="*45)
print("           KEY INSIGHTS")
print("="*45)
print(f"Total Revenue:              ${df['total_price'].sum():,.2f}")
print(f"Average Transaction Value:  ${df['total_price'].mean():,.2f}")
print(f"Total Items Sold:           {df['quantity'].sum():,}")
print(f"Best Branch:                {df.groupby('branch')['total_price'].sum().idxmax()}")
print(f"Best City:                  {df.groupby('city')['total_price'].sum().idxmax()}")
print(f"Top Product Category:       {df.groupby('product_category')['total_price'].sum().idxmax()}")
print(f"Best Selling Product:       {df.groupby('product_name')['quantity'].sum().idxmax()}")
print(f"Dominant Customer Type:     {df['customer_type'].value_counts().idxmax()}")
print(f"Dominant Gender:            {df['gender'].value_counts().idxmax()}")
print("="*45)
print("\nAll 6 charts saved as PNG files!")