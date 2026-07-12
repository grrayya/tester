import csv
import argparse
from pathlib import Path

def get_data(data_file='trials.csv'):
    if not Path(data_file).exists():
        return []
    with open(data_file, 'r') as f:
        return list(csv.DictReader(f))

def filter_stats(target_exp):
    data = get_data()
    # Filter by specific experiment or show all if nothing specified
    subset = [d for d in data if d['experiment'] == target_exp] if target_exp else data
    
    if not subset:
        print("No data found for that query.")
        return

    # Logic to summarize performance
    for entry in subset:
        print(f"[{entry['timestamp'][:10]}] {entry['condition']} | Score: {entry['score']} | {entry['tag']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp", help="Filter by specific experiment")
    args = parser.parse_args()
    
    filter_stats(args.exp)
