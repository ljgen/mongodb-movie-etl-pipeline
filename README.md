# Movie Data ETL Project

## Objective
This project processes movie data from MongoDB, performs transformations to analyze top genres based on ratings and the number of movies, and then visualizes the results. The processed data is also saved in a new MongoDB collection.

## Technologies Used
- **MongoDB** (MongoDB Atlas)
- **Python** (with libraries: `pymongo`, `matplotlib`, `logging`)
- **Environment Variables** (for credentials)
- **Matplotlib** (for static visualizations)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/MongoDBMovieETL.git

2. **Install Dependencies** Navigate to the project directory and install the necessary Python libraries using pip:
   ```bash
   pip install -r requirements.txt
3. **Set up Environment Variables**
   To securely connect to MongoDB Atlas, you need to configure the connection string.
   MongoDB Atlas provides this connection string when you create a cluster.
- **Step 1: Create a MongoDB Atlas Cluster**
  - *1. Go to MongoDB Atlas (https://www.mongodb.com/cloud/atlas).*
  - *2. Log in to your account or create one if you don’t have an account.*
  - *3. Create a new project and a new cluster. Follow the on-screen instructions for setting up your cluster.*
- **Step 2: Get the MongoDB Atlas Connection String**
  - *1. In MongoDB Atlas, click on the "Connect" button for your cluster.*
  - *2. Select "Connect to your application".*
  - *3. Copy the connection string provided (it will look something like this):*
  ```bash
  mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority
  ```
  - *4. Replace <username> and <password> with your actual MongoDB Atlas username and password.*
4. **Run the ETL Pipeline**
   To run the entire ETL (Extract, Transform, Load) process, execute the app.py script, which orchestrates all the steps:
   ```bash
   python app.py
   ```
   This will automatically run the following steps in sequence:
   - **Extract Data:** data_extraction.py - Fetches data from MongoDB.
   - **Transform Data:** data_transformation.py - Cleans and processes the data.
   - **Load Data:** data_load.py - Loads the processed data into a new MongoDB collection.
   - **Visualize Data:** data_visualization.py - Creates a static bar chart of top genres.
   
   By running app.py, all of these tasks will be executed in order, providing a smooth and automated workflow for the ETL process.
## Project Structure
   ```bash
        MovieETLMongoDB/
        ├── scripts/                         # Core scripts for ETL process
        │   ├── data_extraction.py           # Fetches data from MongoDB
        │   ├── data_transformation.py       # Processes and cleans the data
        │   ├── data_load.py                 # Loads the processed data into a new database
        │   ├── data_visualization.py        # Generates static visualizations
        │   ├── db_connection.py             # Database connection handler (includes connect_to_mongodb)
        │   ├── logging_config.py            # Configures logging setup
        ├── app.py                           # Main application script to run the ETL pipeline
        ├── results/                         # Folder for generated results and output
        │   ├── top_genres_chart.png         # Your generated chart
        │   └── processed_data.csv           # Processed data output
        ├── README.md                        # Documentation for the project
        ├── requirements.txt                 # Required dependencies for the project
        └── .env                             # Environment variables (e.g., MongoDB credentials)
   ```
## Project Structure
   - *The project aggregates movie data by genre, calculates the average IMDb rating for each genre, and counts the number of movies per genre.*
   - *Top genres based on ratings and movie count are visualized in a bar chart.*
## Future Work
   - *Implement interactive visualizations using Streamlit.*
   - *Improve data processing logic to handle missing data or edge cases.*
   - *Extend the analysis to include other movie attributes like release year, director, or country.*