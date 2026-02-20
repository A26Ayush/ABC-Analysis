# ABC Analysis Automation Tool

#importing necessary libraries
import streamlit as st
import pandas as pd

# Streamlit app title
st.title("ABC Analysis Automation Tool")

# File uploader for CSV input
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Process the uploaded file
if uploaded_file:
    df = pd.read_csv(uploaded_file)
   
    #Cleaning: Standardize column names
    df.columns = df.columns.str.lower().str.strip()
    
    # Checking the uploaded CSV
    st.subheader("Raw Data")
    st.dataframe(df)
    
    
      # Aggregate duplicates
    df_grouped = df.groupby('sku', as_index=False).agg({
      'quantity': 'sum',
      'price_unit': 'mean',
      'product': 'first'
      })

    # Annual value
    df_grouped['annual_value'] = df_grouped['quantity'] * df_grouped['price_unit']
    df_grouped = df_grouped.sort_values(by='annual_value', ascending=False)

    # Cumulative %
    df_grouped['cumulative_value'] = df_grouped['annual_value'].cumsum()
    total_value = df_grouped['annual_value'].sum()
    df_grouped['cumulative_percent'] = df_grouped['cumulative_value'] / total_value

    # ABC category
    def abc(row):
        if row['cumulative_percent'] <= 0.7:
            return 'A'
        elif row['cumulative_percent'] <= 0.9:
            return 'B'
        return 'C'
    
    # Apply ABC categorization
    df_grouped['ABC_Category'] = df_grouped.apply(abc, axis=1)

    # Display results
    st.subheader("ABC Analysis Results")
    st.dataframe(df_grouped)
    

    # Download option
    csv = df_grouped.to_csv(index=False).encode('utf-8')
    st.download_button("Download Results", csv, "ABC_results.csv", "text/csv")
    
    # Summary by category ABC
    summary = df_grouped.groupby('ABC_Category').agg(
    total_value=('annual_value', 'sum'),
    item_count=('sku', 'count')
    ).reset_index()
    
    # Calculate percentages
    summary['Percent of Total Value'] = summary['total_value'] / total_value
    summary['Percent of Items'] = summary['item_count'] / df_grouped.shape[0]

    # Display summary
    st.subheader("ABC Category Summary")
    st.dataframe(summary)
    
    # Download option for summary
    csv = summary.to_csv(index=False).encode('utf-8')
    st.download_button("Download Summary", csv, "ABC_summary.csv", "text/csv")
    
    # Visualization
    import matplotlib.pyplot as plt

    # Bar chart for total value by ABC category
    fig, ax = plt.subplots()
    ax.bar(summary['ABC_Category'], summary['total_value'], color=['green','orange','red'])
    ax.set_xlabel('ABC Category')
    ax.set_ylabel('Total Value (in ten millions)')
    ax.set_title('ABC Category Value Contribution')
    st.pyplot(fig)
    
    # Use "streamlit run app.py" in terminal to run the app