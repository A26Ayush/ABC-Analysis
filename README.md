**Project Description – Automated ABC Analysis Tool**

This project focuses on automating ABC analysis to help businesses manage inventory more efficiently. The process begins with a raw CSV inventory dataset, which contains information on product SKUs, quantities, and unit costs.

**_Data Preparation_**

Initial cleaning was done in Excel using the Transform Data option, including:

Handling missing values

Removing duplicates

Renaming and standardizing columns

Correcting data types

An additional column for product names/SKUs was added to ensure each item is uniquely identifiable.

**_Python Automation_**

After cleaning, Python and Streamlit were used to automate the ABC analysis workflow:

Calculate annual value for each SKU (Quantity × Unit Cost)

Sort SKUs by value and compute cumulative percentages

Categorize items into A, B, or C based on contribution thresholds (e.g., A: top 70%, B: 70–90%, C: remaining)

Generate interactive charts to visualize the value contribution of each category

**_Outputs_**

Downloadable Excel file with:

1: Full ABC analysis for each SKU

2: Summary of A/B/C categories with total value, percentage of total value, and item count.

_Visualization showing the relative contribution of A, B, and C items_.


_**Business Benefits**_
Identifies high-value (A) products for close monitoring and optimal inventory management.

Helps prioritize ordering and stocking decisions, saving costs and reducing stockouts.

Provides quick insights for managers to allocate resources efficiently.

Enables data-driven decisions through automation and visualization.

This project demonstrates how data cleaning, Python automation, and interactive reporting can simplify inventory management and improve operational efficiency for businesses.


_**Source**_
https://www.kaggle.com/datasets/gajendrasharmagl/sales-data
