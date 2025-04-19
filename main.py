from src.bar_api import get_user_bar
from src.dataset_loader import load_bottle_dataset

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
