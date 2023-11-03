# YouTube Data Analytics Project with AWS

## Overview

This project is aimed at securely managing, streamlining, and performing analysis on structured and semi-structured YouTube video data based on video categories and trending metrics.

## Project Goals

Data Ingestion: Develop a mechanism to ingest data from various sources.
ETL System: Transform raw data into the proper format for analysis.
Data Lake: Create a centralized repository to store data from multiple sources.
Scalability: Ensure the system scales effectively as the data volume increases.
Cloud Integration: Utilize AWS (Amazon Web Services) for processing large amounts of data efficiently.
Reporting: Build a dashboard to extract insights from the data.

## Services Used

I used various AWS services to achieve project goals:

**Amazon S3:** For raw, cleansed and analytic data
**AWS IAM (Identity and Access Management):** Securely manage access to AWS services and resources.
**Amazon QuickSight:** Used for creating the dashboards.
**AWS Glue:** Used for data integration service for data discovery, preparation, and consolidation.
**AWS Lambda: **Computing service for running code without managing servers.
**AWS Athena:** Used for querying data stored in Amazon S3.

## Architecture Diagram

![Alt text](https://github.com/fozgur/YouTube-Data-ETL-Analytics/blob/main/aws-youtubedata-diagram.jpg?raw=true)

## Dataset and Operations

This repository contains a dataset comprising two different types of data files: .csv and .json. These files were initially uploaded to an S3 landing bucket via the CLI. The .csv files contain video details, while the .json files contain category details. The ultimate goal of this project is to create a dashboard using these two datasets, which necessitates some preprocessing steps to optimize the entire process.

### 1. Data Ingestion
The first step involved uploading the dataset files to the S3 landing bucket through the command-line interface (CLI).

### 2. Data Crawling and Exploration
AWS Glue was used to crawl the data, making it accessible for further analysis.
AWS Athena was employed to explore and query the dataset. In this process, some variable type inconsistencies were discovered.

### 3. ETL Job for Data Transformation
To address the variable type inconsistencies and prepare the data for the dashboard, an AWS ETL Job was created. The issue at hand was the need to change variable types, particularly when joining different tables using SQL commands such as cast().

### 4. Data Format Conversion
The .csv and .json files were converted to Parquet format to enhance efficiency during the creation of reports. A Lambda function was utilized for this task.

### 5. Event Trigger for Scalability
A trigger was added to the Lambda function. This trigger was set to activate when a .json file was uploaded to the S3 landing bucket. It dynamically creates a scalable platform.

### 6. Joining Parquet Tables
Another ETL job was created to join the Parquet tables. This step was necessary as the reporting process consistently requires the data in a joined format.

### 7. Dashboard Creation
Finally, a dashboard was created in Amazon QuickSight to visualize and analyze the preprocessed data. A more useful dashboard which contains more valuable insight can be created.

<img width="1186" alt="image" src="https://github.com/fozgur/YouTube-Data-ETL-Analytics/assets/104754779/5f11c149-6aa5-491b-8fda-e87bcfc9b654">
