#%%
from complex_evaluate import evaluate_edoal, jaccard_sim
import os
import pandas as pd

#%% Initialize matchers dictionary
matchers = {}

# Walk through the 'edoal' directory to populate the matchers dictionary
for root, _, files in os.walk('./edoal'):
    for file in files:
        ontology = root.split('/')[-2]
        matcher = root.split('/')[-1]
        pair = file.split('.')[0]

        # Ensure matchers dictionary structure is initialized
        matchers.setdefault(ontology, {}).setdefault(pair, []).append((matcher, f'{root}/{file}'))

#%% Evaluate matchers against references
evaluations = []
reference_count = {}

# Walk through the 'references' directory for evaluation
for root, _, files in os.walk('./references'):
    for file in files:
        ontology = root.split('/')[-1]
        pair = file.split('.')[0]

        # Count references for the ontology
        reference_count[ontology] = reference_count.get(ontology, 0) + 1

        # Evaluate matchers and handle errors gracefully
        for matcher, file_path in matchers.get(ontology, {}).get(pair, []):
            try:
                evaluations.extend([
                    [matcher, 'def', pair, ontology] + list(evaluate_edoal(file_path, f'{root}/{file}')),
                    [matcher, 'def w=0', pair, ontology] + list(evaluate_edoal(file_path, f'{root}/{file}', w=0.0)),
                    [matcher, 'def w=1', pair, ontology] + list(evaluate_edoal(file_path, f'{root}/{file}', w=1.0)),
                    [matcher, 'jaccard', pair, ontology] + list(evaluate_edoal(file_path, f'{root}/{file}', sim_func=jaccard_sim)),
                    [matcher, 'jaccard w=0', pair, ontology] + list(evaluate_edoal(file_path, f'{root}/{file}', w=0.0, sim_func=jaccard_sim)),
                    [matcher, 'jaccard w=1', pair, ontology] + list(evaluate_edoal(file_path, f'{root}/{file}', w=1.0, sim_func=jaccard_sim))
                ])
            except:
                # Handle failed evaluations by appending default values
                evaluations.extend([
                    [matcher, metric, pair, ontology, 0, 0, 0] for metric in
                    ['def', 'def w=0', 'def w=1', 'jaccard', 'jaccard w=0', 'jaccard w=1']
                ])

# Create a DataFrame to hold evaluation results
df = pd.DataFrame(evaluations, columns=['matcher', 'metric', 'pair', 'ontology', 'precision', 'recall', 'f1'])

#%% Analyze evaluation results
metrics = ['def', 'def w=0', 'def w=1', 'jaccard', 'jaccard w=0', 'jaccard w=1']

for metric in metrics:
    metric_df = df[df['metric'] == metric]
    filtered_df = metric_df[metric_df['f1'] != 0]
    grouped_df = filtered_df.groupby(['matcher', 'ontology'])[['precision', 'recall', 'f1']].mean()
    print(f"{metric}")
    print(grouped_df.round(2))
    print()

#%%
