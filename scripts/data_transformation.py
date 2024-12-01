from scripts.logging_config import setup_logging
import logging

# Set up logging
setup_logging()

def transform_data(data):
    """Transform Data"""
    try:
        # Define aggregation pipeline
        pipeline = [
            {
                '$unwind': '$genres'
            },
            {
                '$match': {
                    'imdb.rating': {
                        '$exists': True
                    }
                }
            },
            {
                '$group': {
                    '_id': '$genres',
                    'avg_rating': {
                        '$avg': '$imdb.rating'
                    },
                    'count': {
                        '$sum': 1
                    }
                }
            },
            {
                '$project': {
                    '_id': 1,
                    'count': 1,
                    'avg_rating': {
                        '$round': [
                            '$avg_rating', 2
                        ]
                    },
                    'lastUpdated': '$$NOW'
                }
            },
            {
                '$sort': {
                    'avg_rating': -1
                }
            }
        ]

        # Execute aggregation
        result = list(data.aggregate(pipeline))
        logging.info(f"Aggregation complete. Retrieved {len(result)} records.")

        # Display results
        for i, movie in enumerate(result, start=1):
            print(f"Rank {i} : {movie["_id"]} \n Average rating : {movie["avg_rating"]} \n Total number of movies : {movie["count"]}")

        return result

    except Exception as e:
        logging.error(f"Error during data transformation: {e}")
        print(f"Error during data transformation: {e}")
        exit(1)