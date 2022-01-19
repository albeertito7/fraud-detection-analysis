#  Credit Card Transactions Fraud Detection

Over the years, the usage of credit cards has increased considerably, as it makes it easier for the
user to perform purchases without having to go to an ATM, just over the Internet. This is a direct consequence of what the world is actually suffering, a global digitalization process on all senses.

In every area of life, there are currently lots of technologies involved, even when talking about money transactions as the currencies are becoming digital as well.
But, with the beginning of COVID-19, all has been accelerated, causing at the same time a rise in cybercrime and insecurity among users. For his reason, creating a product that can detect, predict and prevent fraudulent transactions, would make things easier for those companies wondering how to offer security and confidence to their users. 

This repository aims to define, based on the previous premises, the basis for the design and development of a Big Data project, setting the starting point for building a comprhensive model to fill the requirements.

## About the Dataset

This is a simulated credit card transaction dataset containing legitimate and fraud transactions from the duration 1st Jan 2019 - 31st Dec 020. It covers credit cards of 1000 customers doing transactions with a pool of 800 merchants.

## Getting Started

## Project Structure

    ├── LICENSE            <- MIT License.
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── data
    │   ├── interm         <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering), and
    │                         a short `-` delimited description, e.g `1.0-initial-data-exploration`.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment using `pip`.
    ├── environment.yml    <- The configuration file for reproducing the environment using `conda`.
    │
    ├── docker-compose.yml <- To run docker-compose for the creation of the spark environment.
    │
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module.
        │
        └── data           <- Scripts to download or generate data.
            │       
            └── make_dataset.py