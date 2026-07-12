import subprocess
import datetime
import csv
from pathlib import Path

def get_last_commit_date():
    # check git log for today's date
    result = subprocess.run(['git', 'log', '-1', '--format=%cd', '--date=short'], 
                            capture_output=True, text=True)
    return result.stdout.strip()

def auto_record():
    today = datetime.date.today().isoformat()
    if get_last_commit_date() != today:
        print("No commits today, skipping.")
        return

    # log session automatically if commit exists
    with open('trials.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.datetime.now().isoformat(),
            "coding",
            "git_push",
            7,
            7,
            "auto_log"
        ])
    print("Auto-logged coding session.")

if __name__ == "__main__":
    auto_record()
