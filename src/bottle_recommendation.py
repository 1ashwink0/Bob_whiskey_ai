from sklearn.preprocessing import StandardScaler, OneHotEncoder
from scipy.sparse import hstack  # for combining weighted feature matrices
from sklearn.metrics.pairwise import cosine_similarity



def recommend_similar_bottles(user_data, bottles_df, top_n=5):
    print("\n--- PHASE 4: Recommend Similar Bottles ---")

    # Step 1: Extract user's owned bottle data
    collection_products = [b["product"] for b in user_data if "product" in b and "id" in b["product"]]
    if not collection_products:
        print("No user data to base recommendations on.")
        return
    owned_ids = [p["id"] for p in collection_products]

    # Step 2: Define features
    num_features = ["size", "proof", "abv", "popularity", "avg_msrp", "fair_price",
                    "shelf_price", "total_score", "wishlist_count", "vote_count",
                    "bar_count", "ranking"]
    cat_features = ["name", "spirit_type", "brand_id"]

    # Step 3: Separate preprocessing
    num_scaler = StandardScaler()
    cat_encoder = OneHotEncoder(handle_unknown="ignore")

    # Apply preprocessing
    bottles_df = bottles_df.copy()
    features_df = bottles_df[num_features + cat_features].fillna(0)

    scaled_num = num_scaler.fit_transform(features_df[num_features]) * 0.5  # 👈 weight for numerical
    features_df[cat_features] = features_df[cat_features].astype(str)
    encoded_cat = cat_encoder.fit_transform(features_df[cat_features]) * 1.5  # 👈 weight for categorical

    # Combine features with priority given to categorical
    combined_features = hstack([scaled_num, encoded_cat])

    # Step 4: Compute similarity
    similarities = cosine_similarity(combined_features)

    # Step 5: Aggregate scores from owned bottles
    owned_indexes = bottles_df[bottles_df["id"].isin(owned_ids)].index
    similarity_scores = similarities[owned_indexes].mean(axis=0)

    # Step 6: Recommend top-N bottles
    bottles_df["similarity_score"] = similarity_scores
    recommendations = bottles_df[~bottles_df["id"].isin(owned_ids)]\
        .sort_values(by="similarity_score", ascending=False).head(top_n)

    print("\n🎯 Recommended Bottles (Category-Weighted):")
    print(recommendations[["id", "name", "similarity_score", "spirit_type"]])
