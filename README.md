# aws-youtube-data-analysis

## Project Overview

This project leverages AWS services to analyze a structured and semi-structured YouTube dataset obtained from Kaggle. The primary goal is to provide decision-makers with clear and easily accessible insights by analyzing the dataset.

## Project Objectives

The main objectives of this project are as follows:

1. **Data Preparation and Ingestion:**
   - Ingest the YouTube dataset into Amazon S3.
   - Use AWS Glue for data preparation, including cleaning and transforming the dataset.

2. **Serverless Processing:**
   - Implement serverless functions using AWS Lambda for specific data processing tasks.
   - Leverage AWS Lambda for automating tasks such as data enrichment, format conversions, or custom computations.
  
3. **ETL with AWS Glue:**
   - Utilize AWS Glue for efficient Extract, Transform, Load (ETL) processes.
   - Leverage AWS Glue's capabilities for auto-discovering and cataloging data, facilitating seamless ETL workflows.

4. **Querying with SQL:**
   - Utilize AWS Athena for SQL-based queries on the dataset.
   - Enable decision-makers to interactively explore the dataset using familiar SQL syntax.

5. **Visualizations and Reporting:**
   - Employ AWS QuickSight to create interactive and insightful visualizations.
   - Generate reports that convey meaningful trends and patterns in the YouTube data.

6. **Scalability and Efficiency:**
   - Design the project to be scalable, allowing for the analysis of larger datasets in the future.
   - Optimize the use of AWS services to ensure cost-effectiveness and efficient resource utilization.

## Dataset

The dataset used for this project is sourced from Kaggle's Trending YouTube Video Statistics(https://www.kaggle.com/datasets/datasnaek/youtube-new). It encompasses a comprehensive collection of data on trending videos on the YouTube platform.

## AWS Services Used

The project makes use of the following AWS services:

- **Amazon S3:** Utilized for storing the dataset.
  
- **AWS IAM (Identity and Access Management):** Employed for identity management and security settings.
  
- **AWS Glue:** Used for Extract, Transform, Load (ETL) processes on the dataset.
  
- **AWS Lambda:** Employed for serverless functions.
  
- **AWS Athena:** Used for querying the dataset with SQL queries.
  
- **AWS QuickSight:** Utilized for visualizations and reporting.

## Architecture Diagram

![image](https://github.com/oguzhangoktas/aws-youtube-data-analysis/assets/138725663/7bc7aa52-b67d-4760-87c3-973ab2416408)

## 📌 Credits & References

This project was inspired by [Darshil Parmar](https://github.com/darshilparmar)'s excellent YouTube tutorials and GitHub repository:  
🔗 [dataengineering-youtube-analysis-project](https://github.com/darshilparmar/dataengineering-youtube-analysis-project)

I followed the steps provided and implemented this project for learning purposes while also adding my own improvements and documentation.

Thanks to Darshil for the valuable content! 🙌

