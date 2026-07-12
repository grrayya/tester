import csv
import argparse
from pathlib import Path

def get_data(data_file='trials.csv'):
    if not Path(data_file).exists():
        return []
    with open(data_file, 'r') as f:
        return list(csv.DictReader(f))

def show_correlations():
    data = get_data()
    if not data:
        print("No data.")
        return

    summary = {}
    for entry in data:
        tag = entry['tag']
        if tag not in summary:
            summary[tag] = {'scores': [], 'energies': []}
        summary[tag]['scores'].append(int(entry['score']))
        summary[tag]['energies'].append(int(entry['energy']))

    print(f"{'Tag':<15} | {'Avg Score':<10} | {'Avg Energy':<10} | {'Count'}")
    print("-" * 50)
    for tag, stats in summary.items():
        avg_score = sum(stats['scores']) / len(stats['scores'])
        avg_energy = sum(stats['energies']) / len(stats['energies'])
        print(f"{tag:<15} | {avg_score:<10.1f} | {avg_energy:<10.1f} | {len(stats['scores'])}")

if __name__ == "__main__":
    show_correlations()
