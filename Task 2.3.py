import numpy as np
from scipy.spatial.distance import cosine, euclidean, cityblock
from scipy.stats import pearsonr


hassan = np.array([9, 8, 7, 6, 7, 8, 6])
redbull = np.array([10, 9, 6, 7, 6, 9, 5])
ferrari = np.array([9, 7, 6, 6, 7, 7, 5])
mercedes = np.array([8, 6, 8, 9, 9, 5, 9])

teams = {
    "Red Bull": redbull,
    "Ferrari": ferrari,
    "Mercedes": mercedes
}

results = {}

for team, vec in teams.items():
    cos_sim = 1 - cosine(hassan, vec)  # cosine similarity
    euclid = euclidean(hassan, vec)  # Euclidean distance
    manhattan = cityblock(hassan, vec)  # Manhattan distance
    corr, _ = pearsonr(hassan, vec)  # Pearson correlation

    results[team] = {
        "Cosine Similarity": cos_sim,
        "Euclidean Distance": euclid,
        "Manhattan Distance": manhattan,
        "Pearson Correlation": corr
    }


print("=== Similarity Metrics for Hassan ===\n")
for team, metrics in results.items():
    print(f"{team}:")
    for metric, value in metrics.items():
        print(f"  {metric}: {value:.4f}")
    print()


best_team = max(results, key=lambda t: results[t]["Cosine Similarity"])

print("=== Final Recommendation ===")
print(f"Hassan best fits with {best_team}, "
      f"based on highest Cosine Similarity = {results[best_team]['Cosine Similarity']:.4f}")
