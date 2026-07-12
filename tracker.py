import csv
import datetime
from pathlib import Path

class ExperimentLogger:
    def __init__(self, filename="trials.csv"):
        self.file = Path(filename)
        self.exists = self.file.exists()

    def log(self, experiment, condition, score, energy, tag):
        if not self.exists:
            with open(self.file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "experiment", "condition", "score", "energy", "tag"])
            self.exists = True

        with open(self.file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.datetime.now().isoformat(),
                experiment,
                condition,
                score,
                energy,
                tag
            ])
