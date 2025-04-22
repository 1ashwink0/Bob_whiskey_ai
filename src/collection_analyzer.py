def analyze_collection(user_data, bottles_df):
    print("\n--- PHASE 3: Analyze the Collection ---")

    # Create DataFrame from user's collection
    collection = user_data
    collection_ids = [bottle["product"]["id"] for bottle in collection if "product" in bottle]

    bottles_df["id"] = bottles_df["id"].astype(int)
    user_collection_df = bottles_df[bottles_df["id"].isin(collection_ids)]

    if user_collection_df.empty:
        print("No matching bottles found in the dataset for this user.")
        return
    owned_count = len(collection_ids)
    # Show user-owned bottles
    print("\n🍸 User's Collection matching with Dataset:")
    print(user_collection_df[["id", "name", "ranking", "bar_count"]])
    print(f"\n✅ Owned: {owned_count}")
