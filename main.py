from src.bar_api import get_user_bar
from src.dataset_loader import load_bottle_dataset
from src.collection_analyzer import analyze_collection

if __name__ == "__main__":
    username = "your_username_here"  # Replace with real BAXUS username

    # Step 3: Fetch user bar
    try:
        user_bar = get_user_bar(username)
        print("User Bar:", user_bar)
    except Exception as e:
        print(e)

    # Step 4: Load bottle dataset
    try:
        dataset = load_bottle_dataset()
        print(dataset.head())
    except Exception as e:
        print(e)

    # Step 5: Analyse collection
    try:
        user_data = get_user_bar(username)
        bottles_df = load_bottle_dataset()
        analyze_collection(user_data, bottles_df)
    except Exception as e:
        print(e)



