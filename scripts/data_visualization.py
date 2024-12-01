from scripts.logging_config import setup_logging
import matplotlib.pyplot as plt
import logging

# Set up logging
setup_logging()

def visualize_data(result):
    """Visualizations"""
    try:
        # Static Visualizations (Matplotlib)
        counts_sorted = sorted(result, key=lambda x: x["count"], reverse=True)
        top_five_genres = [item["_id"] for item in counts_sorted[:5]]
        top_five_total = [item["count"] for item in counts_sorted[:5]]

        plt.bar(top_five_genres, top_five_total, color="hotpink", width=0.5)
        plt.title("Top 5 Genres by Number of Movies")
        plt.xlabel("Genres")
        plt.ylabel("Number of Movies")
        plt.grid(axis="y")
        plt.show()

        # Interactive Visualizations (Streamlit)

        # Step 6: Advanced Features
        # __________*****__________

    except Exception as e:
        logging.error(f"Error during data visualization: {e}")
        print(f"Error during data visualization: {e}")
        exit(1)