from datasets import Dataset, load_dataset
from ragas import evaluate
from ragas.metrics import (
    context_precision,
    context_recall,
    context_relevance,
    faithfulness,
    answer_relevance,
    context_utilization,
)

# ------------------------------------------------------------
# Step 1. Load your evaluation data
# ------------------------------------------------------------
# Each record should contain:
# - "question": user query
# - "answer": model-generated answer
# - "contexts": list of retrieved text chunks
# - "ground_truth": reference (golden) answer

# Example structure:
# [
#   {
#     "question": "How much revenue does Microsoft generate from contracts with customers?",
#     "answer": "Microsoft's revenue ...",
#     "contexts": ["Revenue allocated to remaining performance ..."],
#     "ground_truth": "Revenue allocated to remaining performance obligations ..."
#   },
#   ...
# ]

dataset = load_dataset("json", data_files="finrag_eval.json")["train"]

# ------------------------------------------------------------
# Step 2. Define metrics
# ------------------------------------------------------------
metrics = [
    context_precision,
    context_recall,
    context_relevance,
    context_utilization,
    faithfulness,
    answer_relevance,
]

# ------------------------------------------------------------
# Step 3. Run evaluation
# ------------------------------------------------------------
results = evaluate(dataset=dataset, metrics=metrics)

# ------------------------------------------------------------
# Step 4. Display results
# ------------------------------------------------------------
print("\n=== FinRAG Evaluation Results ===")
for metric, value in results.items():
    print(f"{metric:25s}: {value:.4f}")

# ------------------------------------------------------------
# Optional: Save results
# ------------------------------------------------------------
with open("finrag_ragas_results.txt", "w") as f:
    for metric, value in results.items():
        f.write(f"{metric}: {value:.4f}\n")

print("\nSaved results to finrag_ragas_results.txt")
