import csv
import matplotlib.pyplot as plt
from pathlib import Path

def plot_trends(data_file='trials.csv'):
    if not Path(data_file).exists():
        return

    with open(data_file, 'r') as f:
        data = list(csv.DictReader(f))

    scores = [int(d['score']) for d in data]
    energies = [int(d['energy']) for d in data]
    
    plt.figure(figsize=(10, 5))
    plt.plot(scores, label='Performance Score', marker='o')
    plt.plot(energies, label='Energy Level', marker='x')
    plt.title('Trial Performance Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_trends()
