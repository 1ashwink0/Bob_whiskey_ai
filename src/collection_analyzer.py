def analyze_collection(user_data, bottles_df):
    print("\n--- PHASE 3: Analyze the Collection ---")

    # Create DataFrame from user's collection
    collection_ids = [str(bottle["id"]) for bottle in user_data.get("collection", [])]
    bottles_df["id"] = bottles_df["id"].astype(str)
    user_collection_df = bottles_df[bottles_df["id"].isin(collection_ids)]

    if user_collection_df.empty:
        print("No matching bottles found in the dataset for this user.")
        return

    # Show user-owned bottles
    print("\n📦 User's Collection:")
    print(user_collection_df[["id", "name", "ranking", "bar_count"]])

    # Analyze tags
    tag_counter = {}
    for bottle in user_data.get("collection", []):
        for tag in bottle.get("tags", []):
            tag_counter[tag] = tag_counter.get(tag, 0) + 1

    print("\n Tag Breakdown:")
    for tag, count in tag_counter.items():
        print(f"{tag.capitalize()}: {count}")

    # Collection Rankings
    avg_rank = user_collection_df["ranking"].astype(float).mean()
    print(f"\n⭐ Average Bottle Ranking: {avg_rank:.2f}")

    # Wishlist count
    wishlist_count = sum('wishlist' in bottle.get("tags", []) for bottle in user_data["collection"])
    owned_count = len(user_data["collection"]) - wishlist_count

    print(f"\n✅ Owned: {owned_count} | ❤️ Wishlist: {wishlist_count}")
