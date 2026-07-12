import argparse
from tracker import ExperimentLogger
from analyze import show_correlations
from visualize import plot_trends

def main():
    parser = argparse.ArgumentParser(description="Trial & Error System")
    subparsers = parser.add_subparsers(dest="command")

    # The 'log' command
    log_parser = subparsers.add_parser("log", help="Log a new trial session")
    log_parser.add_argument("--exp", required=True)
    log_parser.add_argument("--cond", required=True)
    log_parser.add_argument("--score", type=int, required=True)
    log_parser.add_argument("--energy", type=int, required=True)
    log_parser.add_argument("--tag", required=True)

    # The 'analyze' command
    subparsers.add_parser("analyze", help="Show summary stats and correlations")

    # The 'viz' command
    subparsers.add_parser("viz", help="Plot performance trends")

    args = parser.parse_args()

    # Routing the logic based on the command
    if args.command == "log":
        logger = ExperimentLogger()
        logger.log(args.exp, args.cond, args.score, args.energy, args.tag)
        print(f"Logged {args.exp} | {args.cond}")
        
    elif args.command == "analyze":
        show_correlations()
        
    elif args.command == "viz":
        plot_trends()
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
