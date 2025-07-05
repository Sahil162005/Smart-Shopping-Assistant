import os
import json

def write_results_json(graph, path, total_cost, filename):
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    results_data = {
        "path": path,
        "total_cost": total_cost,
        # Add any other data you want to save here
    }

    with open(filename, 'w') as file:
        json.dump(results_data, file, indent=4)
