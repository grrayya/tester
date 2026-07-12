import csv
import datetime
import argparse
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp")
    parser.add_argument("--cond")
    parser.add_argument("--score", type=int)
    parser.add_argument("--energy", type=int)
    parser.add_argument("--tag")
    
    args = parser.parse_args()
    
    # Simple validation for missing inputs
    if not all([args.exp, args.cond, args.score, args.energy, args.tag]):
        print("Missing required fields")
    else:
        logger = ExperimentLogger()
        logger.log(args.exp, args.cond, args.score, args.energy, args.tag)
        print(f"Recorded {args.exp} session: {args.score}/10")
