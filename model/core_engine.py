import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "updated_data.csv")
# Load dataset
df = pd.read_csv(DATA_PATH)

def calculate_score(user, scheme):
    score = 0

    # Age
    if user["age"] >= scheme["min_age"]:
        score += 2

    # Income
    if user["income"] <= scheme["max_income"]:
        score += 3
    else:
        score -= 2

    # Target group
    if user["group"] == scheme["target_group"]:
        score += 4

    # Level preference
    if user["preferred_level"] == scheme["level"]:
        score += 1

    return score


def recommend_schemes(user):
    results = []

    for _, scheme in df.iterrows():
        score = calculate_score(user, scheme)

        results.append({
            "scheme_name": scheme["scheme_name"],
            "details": scheme["details"],
            "benefits": scheme["benefits"],
            "level": scheme["level"],
            "score": score
        })

    result_df = pd.DataFrame(results)
    result_df = result_df.sort_values(by="score", ascending=False)

    return result_df.head(3).to_dict(orient="records")
