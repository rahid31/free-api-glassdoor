# ETL Script: Fetch Employer Reviews and Save to CSV

This Python script utilizes an API to perform an ETL (Extract, Transform, Load) process. It fetches employer reviews from the API, processes the data, and exports it to a CSV file for further analysis. 

---

## Features

- **Extract:** Fetches employer reviews using the [RapidAPI](https://rapidapi.com/) platform.
- **Transform:** Organizes the extracted JSON data into a structured pandas DataFrame.
- **Load:** Exports the processed data into a CSV file with a user-defined save path.

---

## Requirements

- Python 3.12+
- A [RapidAPI](https://rapidapi.com/) account with access to the desired API.
- `.env` file for storing sensitive credentials.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/etl-employer-reviews.git
   cd etl-employer-reviews
