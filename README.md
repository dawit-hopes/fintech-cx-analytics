## 🚀 Customer Experience Analytics for Fintech Apps

This project addresses a real-world data challenge in the rapidly evolving Financial Technology (Fintech) sector. The core objective is to utilize data engineering and Natural Language Processing (NLP) techniques to **quantify and enhance the customer experience** for mobile banking applications.

Acting as a Data Analyst for Omega Consultancy, the goal is to provide three major Ethiopian banks—Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank—with **actionable, data-driven insights** to improve their app features, manage customer complaints, and boost overall user satisfaction and retention.

### **Project Scope and Methodology**

The project is structured around a complete data pipeline, from raw data acquisition to final business recommendations:

1.  **Data Acquisition:** User reviews, ratings, and associated metadata are scraped from the **Google Play Store** for the target mobile banking applications. A minimum of 1,200 reviews are collected to ensure robust analysis.
2.  **Data Engineering & Storage:** The raw text data is preprocessed, cleaned, and then engineered into a structured format. This refined dataset is stored persistently in a **PostgreSQL relational database**, simulating a professional data warehousing workflow.
3.  **Advanced Analytics (NLP):**
      * **Sentiment Analysis:** Reviews are classified (e.g., positive, negative, neutral) using advanced models (like a fine-tuned DistilBERT) to gauge the emotional tone of customer feedback.
      * **Thematic Analysis:** Keywords and phrases are extracted (using techniques like TF-IDF or spaCy) and clustered into overarching themes (e.g., 'Login Errors,' 'Slow Transfers,' 'User Interface') to pinpoint common satisfaction drivers and critical pain points.
4.  **Business Intelligence:** Insights derived from the data are translated into concrete recommendations aligned with specific business scenarios, such as retaining users, enhancing core features, and optimizing support channels (e.g., for AI chatbot integration). Results are communicated via clear, stakeholder-friendly visualizations and a comprehensive report.

This project demonstrates proficiency in full-stack data analysis, encompassing web scraping, scalable data storage, modern NLP, and effective business communication.

-----

## 🛠️ Project Setup Guide

This project uses a standard Python data science setup managed by Conda and integrates with a PostgreSQL database.

### **1. Environment Setup**

The Conda package manager is used to create an isolated environment, ensuring dependencies do not conflict with other projects.

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/dawit-hopes/fintech-cx-analytics.git
    cd fintech-cx-analytics
    ```
2.  **Create and Activate Conda Environment:**
    Use the following commands in your terminal to create the environment named `fintech-cx` and activate it:
    ```bash
    conda create -n fintech-cx python=3.10
    conda activate fintech-cx
    ```
3.  **Install Dependencies:**
    All required Python libraries are listed in the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

### **2. Database Setup**

This project requires a running PostgreSQL instance to complete the data storage task.

1.  **Install PostgreSQL:**
    Ensure you have PostgreSQL installed on your system. Consult the official PostgreSQL documentation for installation instructions for your operating system.
2.  **Create the Database:**
    Connect to your PostgreSQL server (e.g., via `psql` or a GUI like pgAdmin) and execute the following command to create the database used by the project:
    ```sql
    CREATE DATABASE bank_reviews;
    ```
3.  **Configure Connection:**
    Before running the scripts for Task 3 (data insertion), you will need to configure your database connection parameters (hostname, database name, username, password, port) within the relevant Python script (or use environment variables) to allow the application to connect to the `bank_reviews` database.

### **3. File Structure Summary**

The repository is organized for clear separation of concerns:

| Directory/File | Purpose |
| :--- | :--- |
| `data/` | Stores the final, cleaned, and analyzed `reviews_dataset.csv`. |
| `notebook/` | Contains the `scarap.ipynb` notebook for initial exploration and development. |
| `script/` | Houses the core Python scripts (`scrape.py`, `clean_data.py`, `sentiment_analysis.py`). |
| `src/` | Placeholder for any reusable classes or functions (e.g., database connection utility). |
| `tests/` | Directory for unit tests to ensure code reliability. |
| `requirements.txt` | Lists all necessary Python dependencies for the project. |
