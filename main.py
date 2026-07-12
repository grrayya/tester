import argparse
from tracker import ExperimentLogger
from analyze import show_correlations
from visualize import plot_trends
from auto_log import auto_record

def main():
    parser = argparse.ArgumentParser(description="Trial & Error System")
    subparsers = parser.add_subparsers(dest="command")

    log_parser = subparsers.add_parser("log", help="Log a new trial session")
    log_parser.add_argument("--exp", required=True)
    log_parser.add_argument("--cond", required=True)
    log_parser.add_argument("--score", type=int, required=True)
    log_parser.add_argument("--energy", type=int, required=True)
    log_parser.add_argument("--tag", required=True)

    subparsers.add_parser("analyze", help="Show summary stats and correlations")
    subparsers.add_parser("viz", help="Plot performance trends")
    subparsers.add_parser("autolog", help="Auto-log a session if you committed today")

    args = parser.parse_args()

    if args.command == "log":
        if not (0 <= args.score <= 10) or not (0 <= args.energy <= 10):
            print("score and energy must be between 0 and 10")
            return
        logger = ExperimentLogger()
        logger.log(args.exp, args.cond, args.score, args.energy, args.tag)
        print(f"Logged {args.exp} | {args.cond}")

    elif args.command == "analyze":
        show_correlations()

    elif args.command == "viz":
        plot_trends()

    elif args.command == "autolog":
        auto_record()

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
