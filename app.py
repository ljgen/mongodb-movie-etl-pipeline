from scripts.db_connection import connect_to_mongodb, close_connection
from scripts.data_extraction import extract_data
from scripts.data_transformation import transform_data
from scripts.data_load import load_data
from scripts.data_visualization import visualize_data

def main():
    # Step 1: Connect to MongoDB
    client, db = connect_to_mongodb()

    # Step 2: Extract data from MongoDB
    data = extract_data(db)

    # Step 3: Transform the extracted data
    transformed_data = transform_data(data)

    # Step 4: Load processed data into MongoDB
    load_data(client, transformed_data)

    # Step 5: Generate visualizations
    visualize_data(transformed_data)

    # Step 6: Close connection
    close_connection(client)

if __name__ == "__main__":
    main()
