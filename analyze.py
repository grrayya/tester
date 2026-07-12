import csv
from pathlib import Path

def get_stats(data_file='trials.csv'):
    # reading the raw data, ignoring headers
    trials = []
    if not Path(data_file).exists():
        print("No data yet.")
        return

    with open(data_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            trials.append(row)

    # grouping by experiment type to see what's actually working
    grouped = {}
    for t in trials:
        name = t['experiment']
        if name not in grouped:
            grouped[name] = []
        grouped[name].append(int(t['score']))

    for name, scores in grouped.items():
        avg = sum(scores) / len(scores)
        print(f"{name}: {len(scores)} sessions, avg score {avg:.1f}")

if __name__ == "__main__":
    get_stats()
