import csv
import matplotlib.pyplot as plt
from pathlib import Path

def plot_trends(data_file='trials.csv'):
    if not Path(data_file).exists():
        print(f"No data file at {data_file}, nothing to plot.")
        return

    with open(data_file, 'r') as f:
        trials = list(csv.DictReader(f))

    scores, energies = [], []
    for trial in trials:
        try:
            scores.append(int(trial['score']))
            energies.append(int(trial['energy']))
        except (KeyError, ValueError):
            pass

    if not scores:
        print("No valid rows to plot.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(scores, label='Performance Score', marker='o')
    plt.plot(energies, label='Energy Level', marker='x')
    plt.title('Trial Performance Over Time')
    plt.legend()
    plt.grid(True)

    try:
        plt.show()
    except Exception:
        out = 'trials_plot.png'
        plt.savefig(out)
        print(f"No display available, saved plot to {out} instead.")

if __name__ == "__main__":
    plot_trends()
